#!/usr/bin/env python3
"""
Circuit Resistance Readability Test - Simplified Version

Implements effective resistance metric for text readability using sequential discourse graphs.
This version uses sequential graph only (no embeddings) as a proof-of-concept.
"""

from loguru import logger
from pathlib import Path
import json
import sys
import os
import numpy as np
import scipy.linalg
import nltk
import textstat
import time
import gc
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass, asdict

# Download NLTK data silently
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', quiet=True)
    nltk.download('punkt_tab', quiet=True)

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")


@dataclass
class ReadabilityResult:
    """Container for readability scores."""
    text_id: int
    human_score: float
    effective_resistance: float
    flesch_kincaid: float
    smog: float
    coleman_liau: float
    avg_sentence_length: float
    avg_word_length: float
    num_sentences: int
    num_words: int


def setup_environment():
    """Set up memory limits and environment."""
    import resource
    import psutil

    # Container has 46GB RAM, use up to 30GB for safety
    RAM_BUDGET = 30 * 1024**3  # 30GB
    _avail = psutil.virtual_memory().available
    assert RAM_BUDGET < _avail, f"Budget {RAM_BUDGET/1e9:.1f}GB > available {_avail/1e9:.1f}GB"
    resource.setrlimit(resource.RLIMIT_AS, (RAM_BUDGET * 3, RAM_BUDGET * 3))

    logger.info(f"Memory limit set to {RAM_BUDGET/1e9:.1f}GB")


def create_synthetic_dataset(n_texts: int = 50) -> List[Dict]:
    """
    Create a synthetic dataset with texts at different readability levels.
    """
    logger.info(f"Creating synthetic dataset with {n_texts} texts")

    # Define text templates at different complexity levels
    simple_texts = [
        "The cat sat on the mat. It was happy there. The sun shone bright.",
        "Birds fly in the sky. They sing pretty songs. Children love to play.",
        "We went to the park. It was fun. We saw dogs and cats.",
        "Mom baked a cake. It tasted good. We ate it all up.",
        "The dog ran fast. He caught the ball. We played all day.",
    ]

    medium_texts = [
        "The restaurant prepared an elaborate meal for the distinguished guests who arrived promptly at seven o'clock.",
        "Scientists have discovered a remarkable correlation between atmospheric pressure and weather prediction accuracy.",
        "The committee recommended several substantial changes to the proposed legislation regarding environmental protection.",
        "Students demonstrated exceptional performance in mathematics and science during the annual academic competition.",
        "The company implemented innovative strategies to enhance productivity and maximize shareholder value.",
    ]

    complex_texts = [
        "The epistemological implications of quantum mechanics necessitate a paradigmatic reconceptualization of macroscopic phenomena within contemporary theoretical frameworks.",
        "Constitutional jurisprudence regarding substantive due process has evolved considerably since the seminal deliberations of the Warren Court.",
        "The intersectionality of sociolinguistic determinants manifests in complex morphological variations across demographic cohorts.",
        "Philosophical determinism presents ontological challenges that fundamentally undermine conventional interpretations of volitional agency.",
        "Neuroplasticity research demonstrates that cortical reorganization occurs through mechanisms involving synaptic potentiation and axonal sprouting.",
    ]

    dataset = []
    texts_per_level = n_texts // 3

    # Add simple texts (readability score: 1-3)
    for i in range(texts_per_level):
        text = simple_texts[i % len(simple_texts)]
        dataset.append({
            "text_id": len(dataset),
            "text": text,
            "human_readability_score": 1.0 + (i % 3)  # Scores 1-3
        })

    # Add medium texts (readability score: 4-6)
    for i in range(texts_per_level):
        text = medium_texts[i % len(medium_texts)]
        dataset.append({
            "text_id": len(dataset),
            "text": text,
            "human_readability_score": 4.0 + (i % 3)  # Scores 4-6
        })

    # Add complex texts (readability score: 7-10)
    remaining = n_texts - len(dataset)
    for i in range(remaining):
        text = complex_texts[i % len(complex_texts)]
        dataset.append({
            "text_id": len(dataset),
            "text": text,
            "human_readability_score": 7.0 + (i % 4)  # Scores 7-10
        })

    logger.info(f"Created dataset with {len(dataset)} texts")
    return dataset


def compute_sequential_resistance(text: str) -> Tuple[float, Dict]:
    """
    Compute effective resistance using sequential graph only (no embeddings).
    This is a simplified method that connects consecutive sentences.
    """
    sentences = nltk.sent_tokenize(text)
    sentences = [s for s in sentences if len(s.split()) >= 3]
    n = len(sentences)

    if n < 2:
        return 0.0, {"num_sentences": n, "graph_type": "too_short"}

    metadata = {"num_sentences": n, "method": "sequential_only"}

    # Build adjacency matrix for sequential graph (path graph)
    A = np.zeros((n, n))

    # Add edges between consecutive sentences
    for i in range(n - 1):
        A[i, i + 1] = 1.0
        A[i + 1, i] = 1.0

    # Laplacian
    D = np.diag(np.sum(A, axis=1))
    L = D - A

    # Pseudoinverse using scipy.linalg.pinv
    try:
        L_pinv = scipy.linalg.pinv(L)
    except Exception as e:
        logger.warning(f"Pseudoinverse computation failed: {e}")
        return 0.0, {**metadata, "error": str(e)}

    # Kirchhoff index: n * trace(L_pinv)
    try:
        kirchhoff_index = n * np.trace(L_pinv)
    except Exception:
        # Fallback: sum all pairwise resistance distances
        kirchhoff_index = 0
        for i in range(n):
            for j in range(i + 1, n):
                r_ij = L_pinv[i, i] + L_pinv[j, j] - 2 * L_pinv[i, j]
                kirchhoff_index += r_ij

    metadata["kirchhoff_index"] = float(kirchhoff_index)

    # Normalize by number of sentences and invert (higher resistance = more readable = lower difficulty)
    readability_score = kirchhoff_index / n if n > 0 else 0.0
    
    # Invert so higher score = more difficult (matching human scores and baselines)
    # Use negative because we want: more difficult = higher score
    readability_score = -readability_score
    
    metadata["normalized_score"] = float(readability_score)

    return readability_score, metadata


def compute_baseline_metrics(text: str) -> Dict[str, float]:
    """Compute baseline readability metrics."""
    metrics = {}

    try:
        metrics["flesch_kincaid"] = textstat.flesch_kincaid_grade(text)
    except:
        metrics["flesch_kincaid"] = 0.0

    try:
        metrics["smog"] = textstat.smog_index(text)
    except:
        metrics["smog"] = 0.0

    try:
        metrics["coleman_liau"] = textstat.coleman_liau_index(text)
    except:
        metrics["coleman_liau"] = 0.0

    # Compute average sentence length
    sentences = nltk.sent_tokenize(text)
    words = text.split()
    metrics["avg_sentence_length"] = len(words) / len(sentences) if sentences else 0.0
    metrics["avg_word_length"] = np.mean([len(w) for w in words]) if words else 0.0
    metrics["num_sentences"] = len(sentences)
    metrics["num_words"] = len(words)

    return metrics


def evaluate_correlation(scores1: List[float], scores2: List[float]) -> Dict:
    """Compute correlation between two sets of scores."""
    from scipy.stats import pearsonr, spearmanr

    # Filter out invalid values
    valid_pairs = [(s1, s2) for s1, s2 in zip(scores1, scores2)
                   if np.isfinite(s1) and np.isfinite(s2)]
    if len(valid_pairs) < 2:
        return {"pearson_r": 0.0, "pearson_p": 1.0, "spearman_rho": 0.0, "spearman_p": 1.0}

    s1_valid, s2_valid = zip(*valid_pairs)

    try:
        pearson_r, pearson_p = pearsonr(s1_valid, s2_valid)
    except:
        pearson_r, pearson_p = 0.0, 1.0

    try:
        spearman_rho, spearman_p = spearmanr(s1_valid, s2_valid)
    except:
        spearman_rho, spearman_p = 0.0, 1.0

    return {
        "pearson_r": float(pearson_r),
        "pearson_p": float(pearson_p),
        "spearman_rho": float(spearman_rho),
        "spearman_p": float(spearman_p)
    }


def compute_mae_rmse(predictions: List[float], targets: List[float]) -> Dict:
    """Compute MAE and RMSE."""
    valid_pairs = [(p, t) for p, t in zip(predictions, targets)
                   if np.isfinite(p) and np.isfinite(t)]

    if not valid_pairs:
        return {"mae": float('inf'), "rmse": float('inf')}

    preds, targets = zip(*valid_pairs)
    preds = np.array(preds)
    targets = np.array(targets)

    mae = np.mean(np.abs(preds - targets))
    rmse = np.sqrt(np.mean((preds - targets) ** 2))

    return {"mae": float(mae), "rmse": float(rmse)}


@logger.catch(reraise=True)
def main():
    """Main experiment pipeline."""
    setup_environment()

    # Create logs directory
    Path("logs").mkdir(exist_ok=True)

    # Load or create dataset
    logger.info("Loading dataset...")
    dataset = create_synthetic_dataset(n_texts=50)
    logger.info(f"Dataset loaded with {len(dataset)} texts")

    # Process each text
    results = []
    effective_resistances = []
    human_scores = []
    baseline_scores = {
        "flesch_kincaid": [],
        "smog": [],
        "coleman_liau": [],
        "avg_sentence_length": [],
        "avg_word_length": []
    }

    runtimes = []

    for i, item in enumerate(dataset):
        logger.info(f"Processing text {i+1}/{len(dataset)}...")

        text = item["text"]
        human_score = item["human_readability_score"]

        # Time the effective resistance computation
        start_time = time.time()

        # Compute effective resistance (sequential graph only)
        er_score, metadata = compute_sequential_resistance(text)

        runtime = time.time() - start_time
        runtimes.append(runtime)

        # Compute baseline metrics
        baseline = compute_baseline_metrics(text)

        # Store results
        result = ReadabilityResult(
            text_id=item["text_id"],
            human_score=human_score,
            effective_resistance=er_score,
            flesch_kincaid=baseline["flesch_kincaid"],
            smog=baseline["smog"],
            coleman_liau=baseline["coleman_liau"],
            avg_sentence_length=baseline["avg_sentence_length"],
            avg_word_length=baseline["avg_word_length"],
            num_sentences=baseline["num_sentences"],
            num_words=baseline["num_words"]
        )
        results.append(asdict(result))

        effective_resistances.append(er_score)
        human_scores.append(human_score)
        for key in baseline_scores:
            baseline_scores[key].append(baseline[key])

        # Clean up
        del text, er_score, baseline, result
        if i % 10 == 0:
            gc.collect()

    # Compute correlations
    logger.info("Computing correlations...")

    # Effective resistance vs human scores
    er_correlation = evaluate_correlation(effective_resistances, human_scores)

    # Baseline metrics vs human scores
    baseline_correlations = {}
    baseline_errors = {}
    for metric_name, metric_scores in baseline_scores.items():
        baseline_correlations[metric_name] = evaluate_correlation(metric_scores, human_scores)
        baseline_errors[metric_name] = compute_mae_rmse(metric_scores, human_scores)

    # Compute errors for effective resistance (normalize first)
    # Since effective resistance is on a different scale, we need to normalize
    er_normalized = np.array(effective_resistances)
    if np.std(er_normalized) > 0:
        er_normalized = (er_normalized - np.mean(er_normalized)) / np.std(er_normalized)
        human_normalized = (np.array(human_scores) - np.mean(human_scores)) / np.std(human_scores)
        er_errors = compute_mae_rmse(er_normalized.tolist(), human_normalized.tolist())
    else:
        er_errors = {"mae": float('inf'), "rmse": float('inf')}

    # Computational performance
    avg_runtime = np.mean(runtimes)
    min_runtime = np.min(runtimes)
    max_runtime = np.max(runtimes)

    # Prepare output in exp_gen_sol_out schema format
    examples = []
    for result in results:
        example = {
            "input": dataset[result["text_id"]]["text"],
            "output": str(result["human_score"]),
            "predict_effective_resistance": str(result["effective_resistance"]),
            "predict_flesch_kincaid": str(result["flesch_kincaid"]),
            "predict_smog": str(result["smog"]),
            "predict_coleman_liau": str(result["coleman_liau"]),
            "metadata_human_score": result["human_score"],
            "metadata_num_sentences": result["num_sentences"],
            "metadata_num_words": result["num_words"]
        }
        examples.append(example)
    
    output = {
        "metadata": {
            "experiment_name": "effective_resistance_readability",
            "results": {
                "effective_resistance": {**er_correlation, **er_errors},
                "baselines": {
                    metric: {**baseline_correlations[metric], **baseline_errors[metric]}
                    for metric in baseline_correlations
                }
            },
            "ablation_results": {"sequential_only": er_correlation},
            "computational_performance": {
                "avg_runtime_per_doc": float(avg_runtime),
                "min_runtime": float(min_runtime),
                "max_runtime": float(max_runtime),
                "total_runtime": float(sum(runtimes))
            }
        },
        "datasets": [
            {
                "dataset": "synthetic",
                "examples": examples
            }
        ]
    }

    # Save output
    output_path = Path("method_out.json")
    output_path.write_text(json.dumps(output, indent=2))
    logger.info(f"Results saved to {output_path}")

    # Print summary
    logger.info("=" * 60)
    logger.info("EXPERIMENT SUMMARY")
    logger.info("=" * 60)
    logger.info(f"Effective Resistance Correlation:")
    logger.info(f"  Pearson r: {er_correlation['pearson_r']:.4f} (p={er_correlation['pearson_p']:.4f})")
    logger.info(f"  Spearman ρ: {er_correlation['spearman_rho']:.4f} (p={er_correlation['spearman_p']:.4f})")
    logger.info(f"  MAE: {er_errors['mae']:.4f}, RMSE: {er_errors['rmse']:.4f}")
    logger.info("")
    logger.info("Baseline Metrics Correlation:")
    for metric, corr in baseline_correlations.items():
        logger.info(f"  {metric}: r={corr['pearson_r']:.4f}, ρ={corr['spearman_rho']:.4f}")
    logger.info("")
    logger.info(f"Average runtime per document: {avg_runtime:.4f}s")
    logger.info("=" * 60)

    # Cleanup
    del dataset, results
    gc.collect()


if __name__ == "__main__":
    main()
