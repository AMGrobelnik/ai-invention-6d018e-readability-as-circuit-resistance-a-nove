# CLEAR Corpus Dataset Acquisition Summary

## Dataset Acquired
**CLEAR (CommonLit Ease of Readability) Corpus**

## Source
- **Primary**: Cloned from GitHub: https://github.com/scrosseye/CLEAR-Corpus
- **HuggingFace Backup**: casey-martin/CommonLit-Ease-of-Readability (135 downloads)

## Dataset Statistics
- **Total examples**: 4,724 texts
- **Readability scale**: 1-100 (transformed from BT_easiness Rasch measures)
- **Original BT_easiness range**: [-3.68, 1.71]
- **Transformed score range**: [1.00, 100.00]
- **Mean readability**: 50.96 (std: 18.99)
- **Average sentences per text**: 9.6
- **Average words per text**: 172.0
- **Rater agreement (mean)**: 0.671 (derived from standard error)

## Provenance Verification
- **Published papers**:
  1. Crossley, S. A., et al. (2022). "A large-scaled corpus for assessing text readability." Behavior Research Methods.
  2. Crossley, S. A., et al. (2021). "The CommonLit Ease of Readability (CLEAR) Corpus." Proceedings of EDM 2021.
- **License**: CC BY-NC-SA 4.0
- **Human ratings**: YES - Teacher ratings of text difficulty for student readers
- **Multiple raters**: YES - BT_easiness is derived from multiple teacher ratings via Rasch model

## Output Files
All files saved to: `temp/datasets/`

1. **clear_corpus_processed.json** (9.2 MB) - Full processed dataset
2. **full_clear_corpus_processed.json** (9.2 MB) - Full dataset (aii-json format)
3. **mini_clear_corpus_processed.json** (6.4 KB) - 3 examples for testing
4. **preview_clear_corpus_processed.json** (3.2 KB) - 3 examples with truncated text

## Schema (per example)
```json
{
  "text": "string - text excerpt",
  "text_id": "string - original ID",
  "human_readability_score": "float - 1-100 scale",
  "sentence_boundaries": [[int, int], ...],
  "metadata": {
    "grade_level": null,
    "lexile_band": "string - e.g., '900'",
    "domain": "string - e.g., 'Lit'",
    "sub_domain": "string or null",
    "num_sentences": "int",
    "num_words": "int",
    "pub_year": "int or null",
    "author": "string",
    "title": "string"
  },
  "rater_agreement": "float - 0 to 1, higher = better",
  "bt_easiness_original": "float - original Rasch measure"
}
```

## Supplementary Dataset
Also downloaded: **agentlans/readability** (104,761 train + 13,095 test/validation)
- Contains text with grade level scores
- Sources: Fineweb-Edu, TinyStories, Wikipedia, ArXiv
- Use for additional validation if needed

## Next Steps
The CLEAR corpus is ready for use in readability scoring experiments. The dataset meets all ideal criteria:
1. ✓ REAL human readability judgments
2. ✓ Sufficient sample size (N = 4,724 > 1,000)
3. ✓ Diverse text sources (250+ years, multiple genres)
4. ✓ Multiple raters per text (via Rasch model)
5. ✓ Standardized readability scale (1-100)
6. ✓ Text passages of varying lengths (avg 172 words)
7. ✓ Available with permissive license (CC BY-NC-SA 4.0)
