# Effective Resistance for Readability Graphs Research

## Summary

This research artifact provides comprehensive findings on three foundational components for implementing a 'Readability as Circuit Resistance' metric: (1) Computing effective resistance (Kirchhoff index) from graph Laplacian pseudoinverse - identified NetworkX built-in functions (resistance_distance, effective_graph_resistance) and netneurotools library with implementation code examples and numerical stability considerations. (2) Constructing discourse graphs from text - documented three edge construction methods (sequential, similarity-based with SBERT, RST-based), edge weighting schemes, and relevant Python libraries (sentence-transformers, NetworkX, RST parsers). (3) Identifying readability benchmark datasets - compiled detailed comparison of 5 datasets (WeeBit, CLEAR, Newsela, OneStopEnglish, Wikilarge) with sizes, rating scales, access methods, and licensing information. The artifact includes an implementation roadmap with specific library recommendations, sample code for computing resistance scores from text, and an evaluation plan using the CLEAR corpus. Confidence levels are assessed for each finding, and follow-up research questions are provided.

## Research Findings

## Comprehensive Research Findings

### 1. Effective Resistance Computation

The Kirchhoff index (effective graph resistance) is computed as the sum of resistance distances between all node pairs in a graph, which equals n·tr(L⁺) where L⁺ is the Moore-Penrose pseudoinverse of the Laplacian matrix [1, 2]. 

**Python Implementation Options:**

1. **NetworkX (Recommended)**: Provides built-in `nx.effective_graph_resistance(G)` and `nx.resistance_distance(G, nodeA, nodeB)` functions [1]. These handle weight inversion automatically (invert_weight=True), use the algorithm from Ellens et al. (2011) [1], and raise appropriate errors for disconnected graphs.

2. **netneurotools**: Offers `effective_resistance(W)` function that computes full resistance matrix using numpy.linalg.pinv [3]. Documentation warns to 'Test before use' [3].

3. **Manual Implementation**: Construct Laplacian with `nx.laplacian_matrix(G)`, compute pseudoinverse with `scipy.sparse.linalg.pinv(L)`, then Kirchhoff index = trace(L⁺) × n [4]. Laplacian is singular so regular inverse cannot be used [4].

**Numerical Stability**: For large graphs (>1000 nodes), consider fast approximation algorithms that estimate diagonal entries of pseudoinverse in nearly linear time [5].

### 2. Discourse Graph Construction Methods

**Method 1: Sequential Edges** - Connect sentences in order (i to i+1). Simple baseline capturing local coherence but misses long-distance semantic relationships.

**Method 2: Similarity-Based Edges (Recommended)** - Compute cosine similarity between sentence embeddings and add edges where similarity > threshold (e.g., 0.3) [7]. Implementation using sentence-transformers library:
```python
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode(sentences)
# Add edges where cosine similarity > threshold
```
This method balances simplicity with ability to capture semantic structure [7].

**Method 3: RST-Based Edges** - Use Rhetorical Structure Theory parsers (e.g., isanlp_rst [6], feng-hirst-rst-parser) to identify discourse relations and construct edges based on rhetorical structure. Most linguistically motivated but complex to implement [6].

**Edge Weighting Schemes**: (1) Cosine distance: weight = 1 - cosine_distance, (2) Position-based: exponential decay with sentence distance, (3) Discourse relation strength from RST parser, (4) Hybrid combinations.

### 3. Readability Benchmark Datasets

**Dataset Comparison:**

| Dataset | Size | Rating Scale | Access | License |
|----------|------|--------------|--------|---------|
| **CLEAR** | ~5,000 excerpts | Continuous (3rd-12th grade) | GitHub (scrosseye/CLEAR-Corpus) [9] | CC BY-NC-SA 4.0 |
| **WeeBit** | 6,388 texts (3,125 downsampled) | 5 levels (ages 7-16) | GitHub (shlomihod/deep-text-eval) [8] | Research use |
| **Newsela** | 1,911 articles | 5 levels (2nd-12th grade) | Request at newsela.com [8] | Proprietary |
| **OneStopEnglish** | 189 texts × 3 levels | 3 levels (Elem/Inter/Adv) | GitHub (nishkalavallabhi/OneStopEnglishCorpus) [10] | Research use |
| **Wikilarge** | ~296,402 sentences | Simplification pairs | HuggingFace (waboucay/wikilarge) | Various |

**Recommendation**: Use **CLEAR corpus** for primary evaluation because it has open access via GitHub [9], good size (5,000 examples), continuous readability scores (better for regression), and clear licensing (CC BY-NC-SA 4.0) [9].

### 4. Implementation Roadmap

**Graph Construction**: Use similarity-based edges with SBERT embeddings [7], threshold 0.3-0.5 (tune on validation set).

**Resistance Computation**: Use NetworkX's `effective_graph_resistance()` function [1] - simple API, handles edge cases, well-documented.

**Evaluation**: CLEAR corpus [9], metrics: Pearson correlation, RMSE, MAE vs. human ratings, baselines: Flesch-Kincaid, SMOG, BERT-based regressor.

**Sample Code Structure**:
```python
import networkx as nx
from sentence_transformers import SentenceTransformer

class ReadabilityResistanceScorer:
    def __init__(self, threshold=0.3):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.threshold = threshold
    
    def text_to_graph(self, text):
        sentences = [s.strip() for s in text.split('.') if s.strip()]
        G = nx.Graph()
        for i, sent in enumerate(sentences):
            G.add_node(i, sentence=sent)
        embeddings = self.model.encode(sentences)
        for i in range(len(sentences)):
            for j in range(i+1, len(sentences)):
                sim = np.dot(embeddings[i], embeddings[j])
                if sim > self.threshold:
                    G.add_edge(i, j, weight=sim)
        return G
    
    def compute_resistance_score(self, text):
        G = self.text_to_graph(text)
        return nx.effective_graph_resistance(G)
```

### 5. Key Recommendations

**Do's:**
- Use NetworkX's built-in functions for resistance computation [1]
- Apply SBERT (sentence-transformers) for semantic similarity [7]
- Start with CLEAR corpus for evaluation [9]
- Normalize resistance scores for comparability (e.g., divide by n²)

**Don'ts:**
- Don't use directed graphs (NetworkX functions require undirected) [1]
- Don't assume all edges should have equal weight
- Don't ignore disconnected components (effective resistance is infinite)
- Don't rely solely on Newsela (access requires approval) [8]

### 6. Confidence Assessment

**High Confidence** (strong evidence from multiple sources):
- NetworkX has stable, well-documented resistance functions [1]
- CLEAR corpus is publicly accessible via GitHub [9]
- SBERT provides reliable sentence embeddings [7]

**Medium Confidence** (needs empirical validation):
- Optimal graph construction method (multiple valid approaches)
- Similarity threshold selection (0.3-0.5 range suggested)
- Resistance score interpretation (hypothesis: lower = more readable)

**Low Confidence** (speculative, requires experimentation):
- Whether resistance metric will correlate with human judgments
- Computational efficiency for real-time applications
- Generalizability across different text genres and domains

## Sources

[1] [NetworkX effective_graph_resistance Documentation](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.distance_measures.effective_graph_resistance.html) — Official documentation for NetworkX function to compute Kirchhoff index (effective graph resistance) with implementation details, parameters, and examples.

[2] [Effective graph resistance - Ellens et al. 2011](https://www.sciencedirect.com/science/article/abs/pii/S0024379511001443) — Foundational paper defining effective graph resistance, its computation from Laplacian pseudoinverse, and applications in graph analysis.

[3] [netneurotools effective_resistance Documentation](https://netneurotools.readthedocs.io/en/latest/generated/netneurotools.metrics.effective_resistance.html) — Documentation for alternative Python implementation of effective resistance computation using numpy.linalg.pinv for Laplacian pseudoinverse.

[4] [NumPy pinv Documentation](https://numpy.org/doc/stable/reference/generated/numpy.linalg.pinv.html) — Documentation for Moore-Penrose pseudoinverse computation using SVD, relevant for handling singular Laplacian matrices.

[5] [Diagonal of Pseudoinverse of Graph Laplacian - Lu et al. 2023](https://arxiv.org/abs/2310.05527) — Recent paper on fast approximation algorithms for computing diagonal entries of Laplacian pseudoinverse, relevant for large graphs.

[6] [isanlp_rst RST Discourse Parser](https://github.com/tchewik/isanlp_rst) — GitHub repository for Rhetorical Structure Theory discourse parser that can be used for linguistically-motivated graph construction.

[7] [Sentence Transformers Documentation](https://sbert.net/) — Library for computing sentence embeddings (SBERT) used for semantic similarity-based graph construction with pre-trained transformer models.

[8] [Linguistic Features for Readability Assessment - Deutsch et al. 2020](https://arxiv.org/pdf/2006.00377) — Comprehensive paper describing WeeBit and Newsela corpora with details on dataset construction, accessibility, and readability assessment approaches.

[9] [CLEAR Corpus GitHub Repository](https://github.com/scrosseye/CLEAR-Corpus) — Official repository for CommonLit Ease of Readability (CLEAR) corpus with ~5,000 excerpts, readability scores, and metadata available under CC BY-NC-SA 4.0 license.

[10] [OneStopEnglish Corpus - Vajjala & Lučić 2018](https://aclanthology.org/W18-0535/) — Paper introducing OneStopEnglish corpus with 189 texts at three reading levels (Elementary, Intermediate, Advanced) for readability assessment and text simplification.

## Follow-up Questions

- What is the optimal similarity threshold for constructing similarity-based edges in discourse graphs for readability assessment, and how does it vary across different text genres?
- How does the Kirchhoff index correlate with traditional readability metrics (Flesch-Kincaid, SMOG) across different types of text (narrative, expository, technical)?
- Can the resistance metric be computed efficiently for long documents (>50 sentences) using approximation algorithms, and what accuracy is lost compared to exact computation?

---
*Generated by AI Inventor Pipeline*
