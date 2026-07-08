#!/usr/bin/env python3
"""Convert CLEAR Corpus to exp_sel_data_out.json schema format."""
from loguru import logger
from pathlib import Path
import json
import sys
import numpy as np

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

@logger.catch(reraise=True)
def main():
    # Load processed CLEAR corpus
    clear_path = Path("temp/datasets/clear_corpus_processed.json")
    logger.info("Loading CLEAR corpus from %s", clear_path)
    
    with open(clear_path, 'r') as f:
        clear_data = json.load(f)
    
    num_examples = len(clear_data['examples'])
    logger.info("Loaded %d examples", num_examples)
    
    # Convert to exp_sel_data_out schema
    examples = []
    for ex in clear_data['examples']:
        # Input: text excerpt
        input_text = ex['text']
        
        # Output: human readability score (as string per schema)
        output_score = str(ex['human_readability_score'])
        
        # Create example with required fields
        example = {
            "input": input_text,
            "output": output_score,
            "metadata_text_id": ex['text_id'],
            "metadata_rater_agreement": ex['rater_agreement'],
            "metadata_num_sentences": ex['metadata']['num_sentences'],
            "metadata_num_words": ex['metadata']['num_words'],
            "metadata_lexile_band": ex['metadata']['lexile_band'] if ex['metadata']['lexile_band'] else "",
            "metadata_domain": ex['metadata']['domain'] if ex['metadata']['domain'] else "",
            "metadata_pub_year": ex['metadata']['pub_year'] if ex['metadata']['pub_year'] else -1,
            "metadata_bt_easiness_original": ex['bt_easiness_original']
        }
        examples.append(example)
    
    # Create output in exp_sel_data_out schema
    output = {
        "datasets": [
            {
                "dataset": "CLEAR_corpus_readability",
                "examples": examples
            }
        ]
    }
    
    # Save to full_data_out.json
    output_path = Path("full_data_out.json")
    output_path.write_text(json.dumps(output, indent=2))
    logger.info("Saved %d examples to %s", len(examples), output_path)
    
    # Print statistics
    scores = [float(ex['output']) for ex in examples]
    logger.info("Readability score statistics:")
    logger.info("  Mean: %.2f, Std: %.2f", np.mean(scores), np.std(scores))
    logger.info("  Min: %.2f, Max: %.2f", np.min(scores), np.max(scores))
    logger.info("  Median: %.2f", np.median(scores))

if __name__ == "__main__":
    main()
