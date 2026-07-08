#!/usr/bin/env python3
"""Load and standardize readability datasets to exp_sel_data_out.json schema."""

from loguru import logger
from pathlib import Path
import json
import sys
import random

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

@logger.catch(reraise=True)
def load_dataset(file_path: str) -> list:
    """Load a dataset from JSON file."""
    with open(file_path, 'r') as f:
        data = json.load(f)
    logger.info("Loaded {} rows from {}".format(len(data), file_path))
    return data

@logger.catch(reraise=True)
def standardize_onestop_english(data: list, dataset_name: str) -> dict:
    """Standardize OneStopEnglish dataset (SetFit or iastate version)."""
    examples = []
    
    for i, row in enumerate(data):
        # Extract text and label
        text = row.get('text', '')
        label = row.get('label', '')
        label_text = row.get('label_text', '')  # SetFit version has this
        
        # Use label_text if available, otherwise convert label to string
        output = label_text if label_text else str(label)
        
        example = {
            "input": text,
            "output": output,
            "metadata_fold": i % 5,  # 5-fold cross-validation
            "metadata_task_type": "classification",
            "metadata_n_classes": 3,
            "metadata_row_index": i
        }
        examples.append(example)
    
    return {
        "dataset": dataset_name,
        "examples": examples
    }

@logger.catch(reraise=True)
def standardize_readability(data: list, dataset_name: str, split: str) -> dict:
    """Standardize agentlans/readability dataset."""
    examples = []
    
    for i, row in enumerate(data):
        # Extract text and grade
        text = row.get('text', '')
        grade = row.get('grade', 0)
        source = row.get('source', '')
        
        example = {
            "input": text,
            "output": str(grade),  # Convert to string as required by schema
            "metadata_fold": i % 5,
            "metadata_task_type": "regression",
            "metadata_source": source,
            "metadata_row_index": i
        }
        examples.append(example)
    
    return {
        "dataset": "{}_{}".format(dataset_name, split),
        "examples": examples
    }

@logger.catch(reraise=True)
def standardize_weebit(data: list, dataset_name: str) -> dict:
    """Standardize Weebit dataset."""
    examples = []
    
    for i, row in enumerate(data):
        # Extract text and complexity_age_interval
        text = row.get('text', '')
        age_interval = row.get('complexity_age_interval', '')
        
        # Clean up age_interval (might be numeric)
        output = str(age_interval)
        
        example = {
            "input": text,
            "output": output,
            "metadata_fold": i % 5,
            "metadata_task_type": "classification",
            "metadata_row_index": i
        }
        examples.append(example)
    
    return {
        "dataset": dataset_name,
        "examples": examples
    }

@logger.catch(reraise=True)
def main():
    # Set random seed for reproducibility
    random.seed(42)
    
    # Load all datasets
    datasets = []
    
    logger.info("Loading datasets...")
    
    # 1. SetFit/onestop_english (train)
    data = load_dataset("temp/datasets/full_SetFit_onestop_english_train.json")
    standardized = standardize_onestop_english(data, "SetFit_onestop_english_train")
    datasets.append(standardized)
    
    # 2. SetFit/onestop_english (test)
    data = load_dataset("temp/datasets/full_SetFit_onestop_english_test.json")
    standardized = standardize_onestop_english(data, "SetFit_onestop_english_test")
    datasets.append(standardized)
    
    # 3. iastate/onestop_english (train)
    data = load_dataset("temp/datasets/full_iastate_onestop_english_train.json")
    standardized = standardize_onestop_english(data, "iastate_onestop_english")
    datasets.append(standardized)
    
    # 4. agentlans/readability (train)
    data = load_dataset("temp/datasets/full_agentlans_readability_train.json")
    standardized = standardize_readability(data, "agentlans_readability", "train")
    datasets.append(standardized)
    
    # 5. agentlans/readability (test)
    data = load_dataset("temp/datasets/full_agentlans_readability_test.json")
    standardized = standardize_readability(data, "agentlans_readability", "test")
    datasets.append(standardized)
    
    # 6. agentlans/readability (validation)
    data = load_dataset("temp/datasets/full_agentlans_readability_validation.json")
    standardized = standardize_readability(data, "agentlans_readability", "validation")
    datasets.append(standardized)
    
    # 7. Weebit (sampled)
    data = load_dataset("temp/datasets/full_deru35_weebit-authors-grouped-by-age_train_sampled.json")
    standardized = standardize_weebit(data, "weebit_sampled")
    datasets.append(standardized)
    
    # Create output in exp_sel_data_out.json format
    output = {
        "metadata": {
            "description": "Readability datasets for ML-based readability scoring experiment",
            "num_datasets": len(datasets),
            "total_examples": sum(len(d["examples"]) for d in datasets)
        },
        "datasets": datasets
    }
    
    # Save to full_data_out.json
    output_file = "full_data_out.json"
    with open(output_file, 'w') as f:
        json.dump(output, f, indent=2)
    
    logger.info("Saved {} datasets with {} total examples to {}".format(
        len(datasets), output['metadata']['total_examples'], output_file))
    
    # Print summary
    for dataset in datasets:
        logger.info("  - {}: {} examples".format(dataset['dataset'], len(dataset['examples'])))

if __name__ == "__main__":
    main()
