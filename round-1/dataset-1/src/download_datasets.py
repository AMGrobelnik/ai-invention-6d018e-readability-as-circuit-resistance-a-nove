#!/usr/bin/env python3
"""Download readability datasets directly using HuggingFace datasets library."""

from loguru import logger
from pathlib import Path
import json
import sys

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

@logger.catch(reraise=True)
def download_dataset(dataset_id: str, split: str = "train", output_dir: str = "temp/datasets"):
    """Download a dataset and save to JSON files."""
    try:
        from datasets import load_dataset
        
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        logger.info(f"Loading dataset: {dataset_id} (split: {split})")
        dataset = load_dataset(dataset_id, split=split, streaming=False)
        
        # Convert to list of dicts
        data = list(dataset)
        logger.info(f"Loaded {len(data)} rows")
        
        # Save full dataset
        output_file = output_path / f"full_{dataset_id.replace('/', '_')}_{split}.json"
        with open(output_file, 'w') as f:
            json.dump(data, f, indent=2)
        
        logger.info(f"Saved {len(data)} rows to {output_file}")
        
        # Save mini dataset (first 3 rows)
        mini_file = output_path / f"mini_{dataset_id.replace('/', '_')}_{split}.json"
        with open(mini_file, 'w') as f:
            json.dump(data[:3], f, indent=2)
        
        logger.info(f"Saved mini dataset to {mini_file}")
        
        return str(output_file)
        
    except Exception as e:
        logger.error(f"Failed to download {dataset_id}: {e}")
        return None

@logger.catch(reraise=True)
def main():
    datasets_to_download = [
        "SetFit/onestop_english",
        "agentlans/readability",
        "iastate/onestop_english",
        "deru35/weebit-authors-grouped-by-age",
    ]
    
    downloaded_files = []
    
    for dataset_id in datasets_to_download:
        logger.info(f"\n{'='*60}")
        logger.info(f"Downloading: {dataset_id}")
        logger.info(f"{'='*60}")
        
        # Try different splits
        for split in ["train", "test", "validation"]:
            try:
                file_path = download_dataset(dataset_id, split=split)
                if file_path:
                    downloaded_files.append(file_path)
            except Exception as e:
                logger.warning(f"Split {split} not available for {dataset_id}: {e}")
                continue
    
    logger.info(f"\n\nDownloaded {len(downloaded_files)} dataset files")
    for f in downloaded_files:
        logger.info(f"  - {f}")

if __name__ == "__main__":
    main()
