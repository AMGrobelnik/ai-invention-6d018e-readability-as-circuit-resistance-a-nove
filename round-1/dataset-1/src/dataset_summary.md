# Dataset Collection Summary

## Overview
This document summarizes the 4 readability datasets collected for the research experiment on text readability scoring.

## Selected Datasets

### 1. SetFit/onestop_english
- **Source**: HuggingFace Hub
- **Downloads**: 81
- **Description**: OneStopEnglish corpus with 3 reading levels (Elementary, Intermediate, Advanced)
- **Size**: 786KB (train), 1.5MB (test)
- **Rows**: 192 (train), 375 (test)
- **Features**: text, label, label_text
- **Provenance**: Published paper (Vajjala and Lučić, 2018)
- **Green flags**: Established benchmark, clear documentation, 3-class classification

### 2. iastate/onestop_english
- **Source**: HuggingFace Hub
- **Downloads**: 813
- **Likes**: 17
- **Description**: Original OneStopEnglish corpus with 567 texts at 3 reading levels
- **Size**: 2.3MB (train only)
- **Rows**: 567 (train)
- **Features**: text, label
- **Provenance**: Same as above (Vajjala and Lučić, 2018)
- **Green flags**: Most popular version, well-documented

### 3. agentlans/readability
- **Source**: HuggingFace Hub
- **Downloads**: 90
- **Description**: ~200,000 paragraphs with readability grade scores from 4 sources (Fineweb-Edu, TinyStories, Wikipedia, ArXiv)
- **Size**: 101MB (train), 13MB (test), 13MB (validation)
- **Rows**: 104,761 (train), 13,095 (test), 13,095 (validation)
- **Features**: text, grade, source
- **Provenance**: Created by agentlans using established readability formulas
- **Green flags**: Large dataset, multiple sources, continuous grade labels

### 4. deru35/weebit-authors-grouped-by-age (sampled to 10,000 rows)
- **Source**: HuggingFace Hub
- **Downloads**: 62
- **Description**: Weebit corpus grouped by age intervals
- **Size**: 9.8MB (sampled)
- **Rows**: 10,000 (sampled from 1.3M)
- **Features**: text, complexity_age_interval
- **Provenance**: Based on Weebit corpus from BBC Bitesize website (referenced in arXiv:2006.00377)
- **Green flags**: Established readability research dataset

## Dataset Suitability

All 4 datasets are suitable for the proposed method (ML-based readability scoring) because:

1. **Text + Readability Labels**: Each dataset has text passages with associated readability scores/labels
2. **Diverse Sources**: From educational websites (OneStopEnglish) to Wikipedia/ArXiv (agentlans/readability)
3. **Different Label Types**: 
   - Categorical (Elementary/Intermediate/Advanced)
   - Continuous (grade level 0-20)
   - Age interval (3-18+)
4. **Sufficient Size**: From 567 rows to 104,761 rows for training
5. **Under 300MB**: All datasets meet size requirements

## Next Steps

These datasets will be used to:
1. Train and evaluate the proposed ML method for readability scoring
2. Compare performance across different types of readability labels
3. Validate the method on established benchmarks (OneStopEnglish)
4. Test generalization across different text sources

## References

1. Vajjala, S., & Lučić, I. (2018). OneStopEnglish corpus: A new corpus for automatic readability assessment and text simplification. In Proceedings of the Workshop on Automatic Text Simplification.
2. arXiv:2006.00377 - Readability assessment using traditional and neural approaches
3. CommonLit Ease of Readability (CLEAR) Corpus - https://www.commonlit.org/blog/introducing-the-clear-corpus
