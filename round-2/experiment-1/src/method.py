#!/usr/bin/env python3
"""Readability as Circuit Resistance - Experiment Method.

This script implements a novel method for scoring text readability using
graph-based effective resistance (Kirchhoff index) computed from discourse graphs.

Method:
1. Convert text to discourse graph using sentence word overlap for similarity
2. Add edges based on word overlap similarity (Jaccard similarity > threshold)
3. Compute effective graph resistance (Kirchhoff index) using NetworkX
4. Use resistance score as readability metric (lower = more connected = more readable)

Baseline:
- Traditional Flesch-Kincaid Grade Level formula
"""

from loguru import logger
from pathlib import Path
import json
import sys
import gc
import resource
import psutil
import numpy as np
import networkx as nx
import textstat
from sklearn.metrics import mean_absolute_error, mean_squared_error
from scipy.stats import pearsonr

# Constants
SIMILARITY_THRESHOLD = 0.1  # Jaccard similarity threshold
MAX_SENTENCES = 100  # Limit for processing

# Setup logging
logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")


def setup_memory_limits():
    """Set memory limits to prevent OOM kills."""
    try:
        avail_ram = psutil.virtual_memory().available
        ram_budget = int(avail_ram * 0.7)
        resource.setrlimit(resource.RLIMIT_AS, (ram_budget * 3, ram_budget * 3))
        logger.info(f"Set RAM limit to {ram_budget / 1e9:.1f}GB")
    except Exception as e:
        logger.warning(f"Could not set memory limits: {e}")


def text_to_sentences(text: str, max_sentences: int = MAX_SENTENCES) -> list[str]:
    """Split text into sentences using simple rules."""
    import re
    # Split by sentence endings
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    return sentences[:max_sentences]


def get_word_set(sentence: str) -> set[str]:
    """Get set of lowercase words from a sentence."""
    import re
    words = re.findall(r'\b[a-zA-Z]+\b', sentence.lower())
    return set(words)


def build_word_overlap_graph(sentences: list[str], threshold: float = SIMILARITY_THRESHOLD) -> nx.Graph:
    """Build a graph where edges connect sentences with word overlap.
    
    Args:
        sentences: List of sentence strings
        threshold: Jaccard similarity threshold for adding edges
        
    Returns:
        NetworkX Graph with word-overlap-based edges
    """
    if len(sentences) < 2:
        G = nx.Graph()
        if sentences:
            G.add_node(0, sentence=sentences[0])
        return G
    
    G = nx.Graph()
    
    # Add nodes
    for i, sent in enumerate(sentences):
        G.add_node(i, sentence=sent[:50])  # Store truncated sentence
    
    # Precompute word sets
    word_sets = [get_word_set(sent) for sent in sentences]
    
    # Add edges based on Jaccard similarity of word sets
    for i in range(len(sentences)):
        for j in range(i + 1, len(sentences)):
            set_i = word_sets[i]
            set_j = word_sets[j]
            
            if len(set_i) == 0 and len(set_j) == 0:
                similarity = 1.0
            elif len(set_i) == 0 or len(set_j) == 0:
                similarity = 0.0
            else:
                intersection = len(set_i & set_j)
                union = len(set_i | set_j)
                similarity = intersection / union if union > 0 else 0.0
            
            if similarity > threshold:
                G.add_edge(i, j, weight=similarity)
    
    # Ensure graph is connected (add sequential edges if needed)
    if len(sentences) > 1:
        for i in range(len(sentences) - 1):
            if not G.has_edge(i, i + 1):
                G.add_edge(i, i + 1, weight=0.1)  # Low weight for sequential
    
    return G


def compute_effective_resistance(G: nx.Graph) -> float:
    """Compute effective graph resistance (Kirchhoff index)."""
    if G.number_of_nodes() < 2:
        return 0.0
    
    try:
        # Use NetworkX built-in function
        resistance = nx.effective_graph_resistance(G)
        return float(resistance)
    except Exception as e:
        logger.warning(f"Error computing resistance with NetworkX: {e}")
        # Return approximate value based on number of nodes
        # For a path graph: R_eff ≈ n^2 / 2
        # For complete graph: R_eff = 2(n-1)/n
        n = G.number_of_nodes()
        if nx.is_connected(G):
            # Approximate using average shortest path length
            avg_path = nx.average_shortest_path_length(G)
            return float(avg_path * n)
        else:
            # Graph is disconnected - return large value
            return float(n * 10)


def compute_flesch_kincaid_grade(text: str) -> float:
    """Compute Flesch-Kincaid Grade Level (baseline)."""
    try:
        score = textstat.flesch_kincaid_grade(text)
        return float(score)
    except Exception as e:
        logger.warning(f"Error computing Flesch-Kincaid: {e}")
        return 0.0


@logger.catch(reraise=True)
def main():
    """Main function to run the experiment."""
    setup_memory_limits()
    Path("logs").mkdir(exist_ok=True)
    
    # Load data
    data_path = Path(
        "/ai-inventor/aii_data/runs/run_RiHQW43yNEvO/3_invention_loop/"
        "iter_1/gen_art/gen_art_dataset_1/preview_data_out.json"
    )
    
    logger.info(f"Loading data from {data_path}")
    with open(data_path, 'r') as f:
        data = json.load(f)
    
    logger.info(f"Loaded {len(data.get('datasets', []))} datasets")
    
    # Process each dataset
    results = {"metadata": data.get("metadata", {}), "datasets": []}
    
    for dataset_idx, dataset in enumerate(data.get("datasets", [])):
        dataset_name = dataset.get("dataset", f"dataset_{dataset_idx}")
        examples = dataset.get("examples", [])
        
        logger.info(f"Processing dataset: {dataset_name} ({len(examples)} examples)")
        processed_examples = []
        
        for i, example in enumerate(examples):
            if i % 1 == 0:
                logger.info(f"  Processing example {i+1}/{len(examples)}")
            
            text = example.get("input", "")
            
            # Our method: Readability as Circuit Resistance
            try:
                sentences = text_to_sentences(text)
                graph = build_word_overlap_graph(sentences)
                resistance_score = compute_effective_resistance(graph)
                
                # Normalize by number of nodes for comparability
                n = len(sentences)
                normalized_resistance = resistance_score / max(n, 1)
                
                example["predict_our_method"] = str(normalized_resistance)
            except Exception as e:
                logger.error(f"Error in our method for example {i}: {e}")
                example["predict_our_method"] = "0.0"
            
            # Baseline: Flesch-Kincaid Grade Level
            try:
                fk_score = compute_flesch_kincaid_grade(text)
                example["predict_baseline"] = str(fk_score)
            except Exception as e:
                logger.error(f"Error in baseline for example {i}: {e}")
                example["predict_baseline"] = "0.0"
            
            processed_examples.append(example)
            gc.collect()
        
        results["datasets"].append({
            "dataset": dataset_name,
            "examples": processed_examples
        })
        logger.info(f"Completed dataset: {dataset_name}")
    
    # Save results
    output_path = Path("method_out.json")
    logger.info(f"Saving results to {output_path}")
    with open(output_path, 'w') as f:
        json.dump(results, f, indent=2)
    
    # Compute evaluation metrics
    logger.info("Computing evaluation metrics...")
    compute_metrics(results)
    
    logger.info("Experiment completed successfully!")


def compute_metrics(results: dict):
    """Compute evaluation metrics comparing our method and baseline to ground truth."""
    for dataset in results.get("datasets", []):
        dataset_name = dataset.get("dataset", "unknown")
        examples = dataset.get("examples", [])
        
        if not examples:
            continue
        
        our_preds = []
        baseline_preds = []
        ground_truth = []
        
        for ex in examples:
            try:
                output = ex.get("output", "")
                if dataset_name == "SetFit_onestop_english_combined":
                    label_map = {"Elementary": 0, "Intermediate": 1, "Advance": 2}
                    gt = float(label_map.get(output, 0))
                else:
                    gt = float(output)
                
                our_pred = float(ex.get("predict_our_method", 0.0))
                baseline_pred = float(ex.get("predict_baseline", 0.0))
                
                ground_truth.append(gt)
                our_preds.append(our_pred)
                baseline_preds.append(baseline_pred)
            except (ValueError, TypeError) as e:
                logger.warning(f"Could not parse: {e}")
                break
        
        if len(ground_truth) > 0:
            our_preds = np.array(our_preds)
            baseline_preds = np.array(baseline_preds)
            ground_truth = np.array(ground_truth)
            
            logger.info(f"\n=== Metrics for {dataset_name} ===")
            
            # Our method metrics
            try:
                our_mae = mean_absolute_error(ground_truth, our_preds)
                our_rmse = np.sqrt(mean_squared_error(ground_truth, our_preds))
                if len(ground_truth) > 1:
                    our_corr, _ = pearsonr(ground_truth, our_preds)
                else:
                    our_corr = 0.0
                logger.info(f"Our Method (Resistance):")
                logger.info(f"  MAE: {our_mae:.4f}")
                logger.info(f"  RMSE: {our_rmse:.4f}")
                logger.info(f"  Pearson r: {our_corr:.4f}")
            except Exception as e:
                logger.warning(f"Metrics failed for our method: {e}")
            
            # Baseline metrics
            try:
                baseline_mae = mean_absolute_error(ground_truth, baseline_preds)
                baseline_rmse = np.sqrt(mean_squared_error(ground_truth, baseline_preds))
                if len(ground_truth) > 1:
                    baseline_corr, _ = pearsonr(ground_truth, baseline_preds)
                else:
                    baseline_corr = 0.0
                logger.info(f"Baseline (Flesch-Kincaid):")
                logger.info(f"  MAE: {baseline_mae:.4f}")
                logger.info(f"  RMSE: {baseline_rmse:.4f}")
                logger.info(f"  Pearson r: {baseline_corr:.4f}")
            except Exception as e:
                logger.warning(f"Metrics failed for baseline: {e}")


if __name__ == "__main__":
    main()
