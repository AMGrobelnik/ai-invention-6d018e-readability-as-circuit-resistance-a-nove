#!/usr/bin/env python3
"""Sample the Weebit dataset to create a smaller version under 300MB."""

from loguru import logger
from pathlib import Path
import json
import sys

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

@logger.catch(reraise=True)
def sample_dataset(input_file: str, output_file: str, num_samples: int = 10000):
    """Sample a dataset to create a smaller version."""
    logger.info("Sampling {} rows from {}".format(num_samples, input_file))
    
    with open(input_file, 'r') as f:
        data = json.load(f)
    
    logger.info("Total rows in original: {}".format(len(data)))
    
    # Sample rows
    sampled_data = data[:num_samples] if len(data) > num_samples else data
    
    with open(output_file, 'w') as f:
        json.dump(sampled_data, f, indent=2)
    
    logger.info("Saved {} rows to {}".format(len(sampled_data), output_file))
    
    return len(sampled_data)

@logger.catch(reraise=True)
def main():
    # Sample Weebit dataset
    weebit_input = "temp/datasets/full_deru35_weebit-authors-grouped-by-age_train.json"
    weebit_output = "temp/datasets/full_deru35_weebit-authors-grouped-by-age_train_sampled.json"
    
    sample_dataset(weebit_input, weebit_output, num_samples=10000)
    
    logger.info("Sampling complete!")

if __name__ == "__main__":
    main()
