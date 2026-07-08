#!/usr/bin/env python3
"""Process CLEAR Corpus to create standardized dataset with human readability judgments."""
import sys
import json
from pathlib import Path
import pandas as pd
import numpy as np
import nltk
from typing import List, Dict, Any

def main():
    # Download NLTK punkt tokenizer if not available
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt', quiet=True)
    
    # Load CLEAR corpus CSV (already saved from previous step)
    csv_path = Path("temp/datasets/clear_corpus_full.csv")
    print(f"Loading CLEAR corpus from {csv_path}")
    df = pd.read_csv(csv_path)
    print(f"Loaded {len(df)} texts")
    
    # Transform BT_easiness to 1-100 scale as mentioned in plan
    # BT_easiness range: [-3.68, 1.71], mean=-0.96, std=1.03
    # Use min-max normalization to 1-100 scale
    bt_min = df['BT_easiness'].min()
    bt_max = df['BT_easiness'].max()
    df['human_readability_score'] = ((df['BT_easiness'] - bt_min) / (bt_max - bt_min)) * 99 + 1
    
    print(f"Transformed readability scores to 1-100 scale")
    print(f"Score range: [{df['human_readability_score'].min():.2f}, {df['human_readability_score'].max():.2f}]")
    
    # Extract sentence boundaries using simple newline/sentence splitting
    print("Processing texts...")
    results = []
    for idx, row in df.iterrows():
        text = str(row['Excerpt'])
        
        # Use simple sentence splitting on periods, exclamation, question marks
        # This is faster and avoids NLTK dependency issues
        import re
        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
        
        # Calculate sentence boundaries as character offsets
        sentence_boundaries = []
        char_offset = 0
        for sent in sentences:
            start = text.find(sent, char_offset)
            if start == -1:
                start = char_offset
            end = start + len(sent)
            sentence_boundaries.append([start, end])
            char_offset = end
        
        # If no sentences found, use entire text
        if not sentence_boundaries:
            sentence_boundaries = [[0, len(text)]]
        
        # Calculate rater agreement (use s.e. as inverse proxy - lower s.e. = higher agreement)
        # s.e. (standard error) range: [0.07, 1.53] per CLEAR corpus
        rater_agreement = 1.0 / (1.0 + float(row['s.e.']))
        
        # Create output record
        record = {
            "text": text,
            "text_id": str(row['ID']),
            "human_readability_score": float(row['human_readability_score']),
            "sentence_boundaries": sentence_boundaries,
            "metadata": {
                "grade_level": None,  # Not directly available, use Lexile Band
                "lexile_band": str(row['Lexile Band']) if pd.notna(row['Lexile Band']) else None,
                "domain": str(row['Categ']) if pd.notna(row['Categ']) else None,
                "sub_domain": str(row['Sub Cat']) if pd.notna(row['Sub Cat']) else None,
                "num_sentences": int(row['Sentence Count']),
                "num_words": int(row['Google WC']),
                "pub_year": int(row['Pub Year']) if pd.notna(row['Pub Year']) else None,
                "author": str(row['Author']),
                "title": str(row['Title'])
            },
            "rater_agreement": float(rater_agreement),
            "bt_easiness_original": float(row['BT_easiness'])
        }
        results.append(record)
        
        if (idx + 1) % 500 == 0:
            print(f"Processed {idx + 1}/{len(df)} texts")
    
    # Save full dataset
    output_path = Path("temp/datasets/clear_corpus_processed.json")
    output = {"examples": results}
    output_path.write_text(json.dumps(output, indent=2))
    print(f"\nSaved {len(results)} processed examples to {output_path}")
    
    # Generate statistics
    scores = [r['human_readability_score'] for r in results]
    print(f"\n=== Dataset Statistics ===")
    print(f"Total examples: {len(results)}")
    print(f"Readability score - Mean: {np.mean(scores):.2f}, Std: {np.std(scores):.2f}")
    print(f"Readability score - Min: {np.min(scores):.2f}, Max: {np.max(scores):.2f}")
    print(f"Avg sentences per text: {np.mean([r['metadata']['num_sentences'] for r in results]):.1f}")
    print(f"Avg words per text: {np.mean([r['metadata']['num_words'] for r in results]):.1f}")
    print(f"Rater agreement - Mean: {np.mean([r['rater_agreement'] for r in results]):.3f}")

if __name__ == "__main__":
    main()
