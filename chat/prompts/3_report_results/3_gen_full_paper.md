# gen_full_paper — report_results

> Phase: `gen_paper_repo` · `gen_full_paper`
> Run: `run_RiHQW43yNEvO` — Simple Readability Score
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_full_paper` (sdk_openhands_agent)

### [1] SYSTEM-USER prompt · 2026-07-08 12:57:28 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_RiHQW43yNEvO/4_gen_paper_repo/_4_assemble_paper/paper/workspace`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_RiHQW43yNEvO/4_gen_paper_repo/_4_assemble_paper/paper/workspace/`:
GOOD: `/ai-inventor/aii_data/runs/run_RiHQW43yNEvO/4_gen_paper_repo/_4_assemble_paper/paper/workspace/file.py`, `/ai-inventor/aii_data/runs/run_RiHQW43yNEvO/4_gen_paper_repo/_4_assemble_paper/paper/workspace/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>

<task>
Create a publication-ready top-conference LaTeX paper with BibTeX from <paper_text> and <available_figures>, compile to PDF.
</task>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<paper_text>
title: >-
  Readability as Circuit Resistance: A Novel Physically-Motivated Metric Using Effective Graph Resistance
abstract: >-
  Traditional readability formulas rely on surface-level features such as sentence length and word difficulty, while modern
  machine learning approaches operate as black boxes. We propose a novel, physically-motivated readability metric based on
  effective electrical resistance of discourse graphs. We evaluate this approach on the CLEAR corpus (N=4,724 texts with real
  human readability judgments). Results show that the effective resistance metric achieves Pearson correlation r=0.32 with
  human judgments when using sequential graph construction—significant but weaker than traditional formulas (Flesch-Kincaid:
  r=0.50, SMOG: r=0.55). Crucially, we find that the sequential graph construction produces scores functionally equivalent
  to sentence count, meaning the method reduces to a complex reparameterization of text length. Similarity-based graph construction
  produces more differentiated scores but achieves lower correlation (r=0.12). We analyze why the effective resistance metric
  fails to outperform traditional formulas and outline specific improvements for future work.
paper_text: "# Readability as Circuit Resistance: A Novel Physically-Motivated Metric Using Effective Graph Resistance\n\n\
  ## Abstract\n\nTraditional readability formulas rely on surface-level features such as sentence length and word difficulty,\
  \ while modern machine learning approaches operate as black boxes that do not explicitly model the cognitive process of\
  \ reading. We propose a novel, physically-motivated readability metric based on effective electrical resistance of discourse\
  \ graphs. By modeling text as an electrical circuit where sentences are nodes and discourse connections are resistors, the\
  \ total effective resistance (Kirchhoff index) of the graph provides a theoretically grounded measure of readability that\
  \ captures discourse-level coherence. We evaluate this approach on the CLEAR corpus (N=4,724 texts with real human readability\
  \ judgments) and compare against traditional baselines including Flesch-Kincaid, SMOG, and Coleman-Liau. Results show that\
  \ the effective resistance metric achieves Pearson correlation r=0.32 with human judgments when using sequential graph construction—significant\
  \ but weaker than traditional formulas (Flesch-Kincaid: r=0.50, SMOG: r=0.55). Crucially, we find that the sequential graph\
  \ construction produces scores that are functionally equivalent to sentence count (only 39 distinct values, r=-1.00 with\
  \ sentence count), meaning the method reduces to a complex reparameterization of text length. Similarity-based graph construction\
  \ using TF-IDF cosine similarity produces more differentiated scores (1,534 distinct values) but achieves lower correlation\
  \ (r=0.12). We analyze why the effective resistance metric fails to outperform traditional formulas and outline specific\
  \ improvements for future work, including the use of neural sentence embeddings and rhetorical structure theory (RST) parsers\
  \ for graph construction.\n\n**Keywords:** readability assessment, effective resistance, graph theory, discourse coherence,\
  \ Kirchhoff index\n\n\n## 1 Introduction\n\nAssessing the readability of text is a fundamental problem in natural language\
  \ processing with applications spanning education, content creation, and accessibility [1]. Traditional readability formulas\
  \ such as Flesch-Kincaid [2], SMOG [3], and Coleman-Liau [4] have been used for decades, relying primarily on surface features:\
  \ sentence length, word length, and syllable counts. While these formulas are simple and interpretable, they fail to capture\
  \ deeper structural and coherence properties of text that influence reading comprehension [5].\n\nRecent advances in machine\
  \ learning have produced more accurate readability models using neural architectures [6]. However, these approaches typically\
  \ function as black boxes, learning implicit features from data without providing interpretable insights into *why* a text\
  \ is difficult or easy to read. This limits their utility in educational settings where explainability is important.\n\n\
  A critical missing element in existing approaches is an explicit model of the *cognitive process of reading*. When humans\
  \ read, they construct a coherent mental representation of the text by connecting sentences and integrating information\
  \ across discourse units. Texts with strong discourse coherence—where sentences are tightly connected through semantic relationships—are\
  \ easier to comprehend because information flows smoothly between ideas. Conversely, disjointed or poorly structured text\
  \ impedes comprehension because readers must work harder to bridge gaps between ideas.\n\nWe propose to model this \"information\
  \ flow\" using concepts from electrical network theory. In electrical circuits, current flows easily through pathways with\
  \ low resistance, while high-resistance pathways impede current flow. Analogously, we hypothesize that readable text creates\
  \ \"low-resistance pathways\" for information flow through coherent discourse connections, while complex or incoherent text\
  \ presents \"high-resistance\" to comprehension.\n\nSpecifically, we represent text as a graph where sentences are nodes\
  \ and discourse connections are weighted edges (resistors). The *effective resistance* (also known as the Kirchhoff index)\
  \ of this graph—a global graph invariant derived from the pseudoinverse of the Laplacian matrix—provides our readability\
  \ score. Intuitively, graphs with many short, well-connected pathways between sentences have low effective resistance (easy\
  \ information flow = readable), while graphs with sparse or long paths have high effective resistance (impeded flow = difficult).\n\
  \nOur main contributions are:\n\n1. **A novel physically-motivated readability metric** based on effective electrical resistance\
  \ of discourse graphs, providing an interpretable alternative to traditional formulas and black-box models.\n\n2. **Honest\
  \ empirical evaluation** on the CLEAR corpus (N=4,724 texts with real human judgments), showing that the effective resistance\
  \ metric achieves Pearson correlation r=0.32 with human judgments using sequential graph construction—significant (p < 10^-115)\
  \ but weaker than traditional formulas.\n\n3. **Analysis of a critical failure mode**: We demonstrate that the sequential\
  \ graph construction (sentence i connected to i+1) produces scores that are functionally equivalent to sentence count, providing\
  \ only 39 distinct values across the dataset. This means the method, in its simplest form, reduces to a complex way to measure\
  \ text length.\n\n4. **Evaluation of similarity-based graph construction** using TF-IDF cosine similarity between sentences,\
  \ which produces more differentiated scores but achieves lower correlation (r=0.12), suggesting that simple word-overlap\
  \ similarity is insufficient for capturing discourse coherence.\n\n5. **Open-source implementation** of the effective resistance\
  \ readability scorer, enabling reproducibility and future research.\n\nThe remainder of this paper is organized as follows.\
  \ Section 2 reviews related work in readability assessment and graph-based coherence modeling. Section 3 formalizes the\
  \ effective resistance metric and describes our graph construction approaches. Section 4 presents the experimental evaluation\
  \ on the CLEAR corpus, including honest reporting of negative results. Section 5 discusses why the method fails to outperform\
  \ traditional formulas and outlines specific improvements. Section 6 concludes.\n\n\\footnote{Code: \\url{https://github.com/AMGrobelnik/ai-invention-6d018e-readability-as-circuit-resistance-a-nove/tree/main/round-2/dataset-1}}\n\
  \n\n## 2 Related Work\n\n### 2.1 Traditional Readability Formulas\n\nTraditional readability assessment relies on surface-level\
  \ linguistic features. The Flesch Reading Ease formula [2] computes a weighted combination of average sentence length and\
  \ average word syllables. The Flesch-Kincaid Grade Level [7] adapts this for educational grade levels. The SMOG index [3]\
  \ counts polysyllabic words, while the Coleman-Liau index [4] uses character-level features. These formulas are widely used\
  \ due to their simplicity but have well-documented limitations: they assume linear relationships between features and comprehension,\
  \ ignore discourse structure, and fail on texts with non-standard syntax [5].\n\n### 2.2 Graph-Based Coherence Modeling\n\
  \nRecent work has applied graph theory to model textual coherence. Mesgar and Strube [8] propose graph-based coherence features\
  \ for readability assessment, using entity grids and discourse relation graphs with features like outdegree and frequent\
  \ subgraphs. However, their approach uses local graph patterns rather than global spectral properties. Guinaudeau and Strube\
  \ [9] introduce entity graphs and one-mode projections for coherence modeling, but similarly focus on local edge statistics.\n\
  \nOur work differs fundamentally from these approaches: instead of extracting local graph features, we compute the *effective\
  \ resistance* of the entire graph—a global spectral property that captures overall connectivity and information flow capacity.\
  \ This provides a single, interpretable scalar metric grounded in electrical network theory.\n\n### 2.3 Deep Learning for\
  \ Readability\n\nZhang et al. [6] propose a graph-based readability assessment method using Graph Convolutional Networks\
  \ (GCNs) on part-of-speech dependency graphs. While their approach leverages graph structure, it requires training deep\
  \ networks that learn features implicitly. In contrast, our effective resistance metric is *parameter-free* and directly\
  \ interpretable: the Kirchhoff index has a clear physical meaning as the total resistance to information flow.\n\n### 2.4\
  \ Information-Theoretic Approaches\n\nEhret [10] proposes using Kolmogorov complexity (via text compression) as a universal\
  \ measure of language complexity. While both approaches use information theory concepts, effective resistance captures *discourse-level\
  \ connectivity* while Kolmogorov complexity captures *lexical/syntactic redundancy*. The two approaches are complementary\
  \ and could be combined in future work.\n\n### 2.5 Cognitive Models of Readability\n\nKlein et al. [5] demonstrate that\
  \ surprisal (from language models) predicts reading ease measured via eye tracking. Our approach is complementary: effective\
  \ resistance models *discourse structure* while surprisal models *lexical predictability*. Integrating both signals could\
  \ yield a more complete cognitive model of readability.\n\n\n## 3 Methods\n\n### 3.1 Preliminaries: Effective Resistance\
  \ and the Kirchhoff Index\n\nThe effective resistance between two nodes in a graph is derived from electrical network theory.\
  \ Consider a graph G = (V, E) with |V| = n nodes. Assigning unit resistors to each edge, the *resistance distance* R_ij\
  \ between nodes i and j is the effective electrical resistance that would be measured between those nodes if the graph were\
  \ an electrical circuit.\n\nThe *Kirchhoff index* (or effective graph resistance) is defined as the sum of resistance distances\
  \ between all pairs of nodes:\n\n$$Kf(G) = \\sum_{i < j} R_{ij}$$\n\nThis can be computed efficiently from the graph Laplacian.\
  \ Let A be the adjacency matrix and D = diag(∑_j A_ij) be the degree matrix. The graph Laplacian is L = D - A. The Moore-Penrose\
  \ pseudoinverse L^+ of L satisfies:\n\n$$R_{ij} = L^+_{ii} + L^+_{jj} - 2L^+_{ij}$$\n\nThe Kirchhoff index is then:\n\n\
  $$Kf(G) = n \\cdot \\text{tr}(L^+) = \\sum_{i=1}^n L^+_{ii}$$\n\nwhere n is the number of nodes [11].\n\nIntuitively, graphs\
  \ that are well-connected (many short paths between nodes) have low effective resistance, while sparse or poorly connected\
  \ graphs have high effective resistance. We hypothesize that this property correlates with readability: coherent, well-structured\
  \ text creates a \"low-resistance\" discourse graph, while disjointed text creates \"high-resistance.\"\n\n### 3.2 Discourse\
  \ Graph Construction\n\nA critical design choice is how to construct the discourse graph from text. We investigate two approaches,\
  \ with a third proposed for future work.\n\n#### 3.2.1 Sequential Graph\n\nThe simplest approach connects sentences in sequential\
  \ order: node i is connected to node i+1 for all i. Edge weights are uniform (1.0 in our implementation). This captures\
  \ local coherence but misses long-distance semantic relationships. \n\n**Important limitation**: For a path graph (sequential\
  \ edges only), the Kirchhoff index has a closed-form expression: Kf(P_n) = (n^3 - n) / 3, where n is the number of nodes\
  \ (sentences). This means the effective resistance is a *deterministic function of sentence count alone*—it adds no information\
  \ beyond what sentence count provides. We analyze this limitation extensively in Section 4.\n\n#### 3.2.2 Similarity-Based\
  \ Graph\n\nWe compute pairwise similarity between sentence representations and add edges where similarity exceeds a threshold\
  \ τ. Edge weights are set to the similarity value. This captures semantic relatedness regardless of sentence position. \n\
  \nIn our implementation, we use two similarity measures:\n- **TF-IDF cosine similarity**: Sentences are represented as TF-IDF\
  \ vectors, and pairwise cosine similarity is computed. Edges are added where similarity exceeds τ = 0.05.\n- **Word overlap\
  \ (Jaccard similarity)**: The Jaccard similarity of word sets between sentences is computed, and edges are added where Jaccard\
  \ > τ = 0.1.\n\nThe threshold τ controls graph density: higher τ yields sparser graphs.\n\n#### 3.2.3 RST-Based Graph (Proposed\
  \ for Future Work)\n\nRhetorical Structure Theory (RST) parsers identify discourse relations between text spans (e.g., *elaboration*,\
  \ *contrast*, *cause*). Edges are added based on these relations, with weights reflecting relation strength from parser\
  \ confidence scores. We were unable to implement this due to the unavailability of reliable RST parsers in our experimental\
  \ environment, but we outline this as a key direction for future work (Section 5.2).\n\n\\footnote{Code: \\url{https://github.com/AMGrobelnik/ai-invention-6d018e-readability-as-circuit-resistance-a-nove/tree/main/round-1/research-1}}\n\
  \n### 3.3 Algorithm\n\nAlgorithm 1 summarizes the effective resistance readability scoring procedure.\n\n```\nAlgorithm\
  \ 1: Effective Resistance Readability Scoring\nInput: Text T\nOutput: Readability score R(T)\n\n1. Sentence-tokenize T →\
  \ sentences s₁, ..., sₙ\n2. if n < 2 then return 0  // Too short to assess\n3. Construct graph G = (V, E):\n   // Option\
  \ A: Sequential edges (baseline)\n   for i = 1 to n-1 do\n       E = E ∪ {(i, i+1)} with weight 1.0\n   // Option B: Similarity\
  \ edges\n   for all pairs (i, j) where i < j do\n       if similarity(s_i, s_j) > τ then\n           E = E ∪ {(i, j)} with\
  \ weight similarity(s_i, s_j)\n4. Compute effective graph resistance:\n   R_eff(G) = effective_graph_resistance(G)\n5. Normalize:\
  \ R(T) = -R_eff(G) / n²\n6. return R(T)\n```\n\nThe normalization in step 5 divides by n² to control for the quadratic scaling\
  \ of the Kirchhoff index with the number of nodes. The negation makes higher scores correspond to more difficult (less readable)\
  \ text, matching the convention used by traditional readability formulas. The choice of n² normalization (rather than n\
  \ or nC2) is motivated by the theoretical scaling: for a path graph, Kf ∼ n³, so dividing by n² gives ∼n scaling, which\
  \ approximates the per-node contribution to reading difficulty.\n\n\n### 3.4 Computational Complexity\n\nComputing the pseudoinverse\
  \ of the Laplacian matrix costs O(n³) for dense matrices. For sparse graphs (e.g., sequential edges only), the Laplacian\
  \ is also sparse, and the NetworkX implementation uses spectral methods that are more efficient for sparse graphs. In practice,\
  \ for typical document lengths (n < 100 sentences), direct computation is sufficiently fast.\n\n\\footnote{Code: \\url{https://github.com/AMGrobelnik/ai-invention-6d018e-readability-as-circuit-resistance-a-nove/tree/main/round-2/experiment-1}}\n\
  \n\n## 4 Experiments\n\n### 4.1 Dataset\n\nWe evaluate our approach on the CLEAR (CommonLit Ease of Readability) corpus\
  \ [12], which contains 4,724 text excerpts with real human readability judgments. Unlike synthetic datasets or algorithmically-assigned\
  \ readability scores, CLEAR provides genuine human assessments from teachers and education experts. The texts span a wide\
  \ range of sources (literature, informational text, textbooks) and time periods (250+ years). Readability scores are on\
  \ a 1-100 scale (higher = more readable), transformed from the original -3 to +3 Rasch model estimates.\n\nKey statistics\
  \ of the CLEAR corpus:\n- N = 4,724 texts\n- Score range: 1.0 - 100.0 (mean = 51.0, std = 18.9)\n- Sentence count range:\
  \ 2 - 41 (mean = 10.0, std = 4.7)\n- Word count range: 19 - 834 (mean = 172, std = 95)\n\n\n\n### 4.2 Baselines\n\nWe compare\
  \ against five established readability metrics:\n\n1. **Flesch-Kincaid Grade Level** [7]: Uses average sentence length and\
  \ average word syllables. We learn a linear mapping from Flesch-Kincaid scores to the CLEAR 1-100 scale for fair comparison.\n\
  2. **SMOG Index** [3]: Counts polysyllabic words (words with 3+ syllables). Linear mapping to CLEAR scale.\n3. **Coleman-Liau\
  \ Index** [4]: Uses character-level features. Linear mapping to CLEAR scale.\n4. **Average Sentence Length**: Simple baseline\
  \ using only sentence length.\n5. **Average Word Length**: Simple baseline using only word length.\n\nAll baselines except\
  \ average sentence/word length are computed using the `textstat` library and mapped to the CLEAR scale via linear regression\
  \ for fair comparison.\n\n### 4.3 Evaluation Metrics\n\nWe report:\n\n- **Pearson correlation coefficient** (r): Measures\
  \ linear agreement between predicted and human scores.\n- **Spearman rank correlation** (ρ): Measures monotonic agreement\
  \ (more robust to outliers).\n- **p-value**: Tests statistical significance of correlations.\n- **Mean Absolute Error (MAE)**\
  \ and **Root Mean Square Error (RMSE)**: Measure prediction accuracy on the CLEAR 1-100 scale.\n\n### 4.4 Results\n\nTable\
  \ 1 presents the main results on the CLEAR corpus (N=4,724).\n\n| Method | Pearson r | Spearman ρ | p-value | MAE | RMSE\
  \ |\n|--------|------------|------------|--------|-----|------|\n| **Proposed Methods** | | | | | |\n| Sequential Graph\
  \ ER | 0.32 | 0.33 | < 10^-115 | 14.53 | 17.97 |\n| TF-IDF Similarity Graph ER | 0.12 | 0.13 | < 10^-16 | 15.40 | 18.86\
  \ |\n| **Traditional Formulas (mapped)** | | | | | |\n| Flesch-Kincaid | 0.50 | 0.53 | < 10^-297 | 13.14 | 16.44 |\n| SMOG\
  \ | 0.55 | 0.56 | < 10^-300 | 12.69 | 15.87 |\n| Coleman-Liau | 0.48 | 0.49 | < 10^-267 | 13.36 | 16.69 |\n| **Simple Baselines**\
  \ | | | | | |\n| Sentence Count | 0.32 | 0.33 | < 10^-115 | 14.53 | 17.97 |\n| Average Word Length | 0.42 | 0.43 | < 10^-200\
  \ | 13.72 | 17.12 |\n\nTable 1: Correlation results on CLEAR corpus (N=4,724). All correlations are statistically significant\
  \ at p < 0.001. The effective resistance metrics (Sequential Graph and TF-IDF Similarity Graph) are compared against traditional\
  \ formulas and simple baselines. Values in the table are computed after learning a linear mapping from each method's score\
  \ to the CLEAR 1-100 scale.\n\nKey findings:\n\n1. **Sequential Graph ER performs equivalently to sentence count**: The\
  \ sequential graph method achieves r=0.32, which is identical to the correlation of raw sentence count with human scores\
  \ (r=0.32). This is because the Kirchhoff index for a path graph is a deterministic function of the number of nodes: Kf(P_n)\
  \ = (n^3 - n) / 3. After our normalization (-Kf/n²), the score is a deterministic function of n alone. The method thus provides\
  \ no information beyond sentence count.\n\n2. **TF-IDF Similarity Graph ER performs poorly**: The similarity-based graph\
  \ construction achieves only r=0.12, much lower than traditional formulas. While this variant produces more differentiated\
  \ scores (1,534 distinct values vs. 39 for sequential), the similarity edges fail to capture meaningful variance in readability.\
  \ We hypothesize that TF-IDF cosine similarity is too shallow a measure of semantic relatedness to capture discourse coherence.\n\
  \n3. **Traditional formulas substantially outperform our method**: Flesch-Kincaid (r=0.50), SMOG (r=0.55), and Coleman-Liau\
  \ (r=0.48) all achieve significantly higher correlation with human judgments. This suggests that surface-level features\
  \ (sentence length, word difficulty) remain strong predictors of readability, and that our graph-theoretic approach in its\
  \ current form does not capture additional signal.\n\n\n\nFigure 1 shows a scatter plot of Sequential Graph ER scores versus\
  \ human readability judgments on the CLEAR corpus. The scores cluster into discrete bands corresponding to sentence counts\
  \ (each band contains texts with the same number of sentences), illustrating that the method reduces to measuring sentence\
  \ count.\n\n[FIGURE:fig1]\n\nFigure 2 compares the Pearson correlation coefficients across all evaluated readability metrics.\
  \ Traditional formulas (orange) substantially outperform the effective resistance methods (blue).\n\n[FIGURE:fig2]\n\n\n\
  ### 4.5 Computational Performance\n\nWe measure runtime on the CLEAR corpus (4,724 texts, 2-41 sentences per text). Results:\n\
  \n- **Average runtime per document**: 1.1 ms\n- **Minimum runtime**: 0.2 ms (2-sentence text)\n- **Maximum runtime**: 8.7\
  \ ms (41-sentence text)\n- **Total runtime for 4,724 documents**: 5.2 seconds\n\nThese results demonstrate that the effective\
  \ resistance metric is computationally efficient, meeting real-time applicability requirements. The O(n³) pseudoinverse\
  \ computation is not a bottleneck for typical document lengths (n < 50 sentences).\n\nFigure 3 shows the runtime scaling\
  \ with number of sentences. Even for the longest documents (41 sentences), runtime remains under 10 ms, confirming computational\
  \ feasibility.\n\n[FIGURE:fig3]\n\n\n### 4.6 Ablation Study: Graph Construction Methods\n\nWe compare the two graph construction\
  \ methods implemented in this study:\n\n1. **Sequential Graph** (Section 3.2.1): Edges only between adjacent sentences.\
  \ Produces 39 distinct score values (matching the number of distinct sentence counts in the dataset).\n\n2. **TF-IDF Similarity\
  \ Graph** (Section 3.2.2): Edges added based on TF-IDF cosine similarity > 0.05. Produces 1,534 distinct score values.\n\
  \nWhile the similarity graph produces more differentiated scores, it achieves lower correlation with human judgments (r=0.12\
  \ vs. r=0.32). This suggests that the similarity edges, as constructed, do not capture meaningful discourse coherence signal.\
  \ The reduced correlation may also reflect that the method now captures variance unrelated to readability.\n\nA proper ablation\
  \ would require a graph construction method that (a) produces differentiated scores, and (b) captures actual discourse coherence.\
  \ We were unable to implement such a method in this study (see Section 5.2 on RST-based graphs) but outline this as critical\
  \ future work.\n\n\n## 5 Discussion\n\n### 5.1 Interpretation of Results\n\nThe honest evaluation on the CLEAR corpus reveals\
  \ that our proposed effective resistance metric, in its current form, does not outperform traditional readability formulas.\
  \ Specifically:\n\n1. **The sequential graph construction is degenerate**: For a path graph, the Kirchhoff index is a closed-form\
  \ function of the number of nodes. This means the \"novel\" metric reduces to a complex nonlinear transformation of sentence\
  \ count. While the correlation with human judgments (r=0.32) is statistically significant, it is not meaningful as a new\
  \ metric.\n\n2. **Similarity-based graph construction using TF-IDF is insufficient**: TF-IDF cosine similarity captures\
  \ lexical overlap but not semantic relatedness. Two sentences can have zero TF-IDF similarity (no shared words) while being\
  \ semantically tightly connected (e.g., \"The cat sat on the mat.\" and \"The feline rested on the rug.\"). Capturing true\
  \ semantic relatedness requires neural sentence embeddings (e.g., SBERT [13]).\n\n3. **Traditional formulas remain strong\
  \ baselines**: The success of Flesch-Kincaid (r=0.50) and SMOG (r=0.55) confirms that surface-level features—sentence length\
  \ and word difficulty—are the primary drivers of perceived readability. A graph-theoretic metric must capture *incremental*\
  \ signal beyond these features to be valuable.\n\n### 5.2 Why the Method Fails: Specific Analysis\n\nWe identify three specific\
  \ reasons why the effective resistance metric underperforms in our evaluation:\n\n1. **Degenerate graph construction (sequential\
  \ graph)**: As noted above, the path graph's Kirchhoff index is determined entirely by the number of nodes. This is a fundamental\
  \ property of the path graph, not a bug in our implementation. The solution is to use graph constructions where the effective\
  \ resistance depends on more than just the number of nodes—specifically, similarity-based edges that create graphs with\
  \ varying connectivity patterns for the same number of nodes.\n\n2. **Insufficient similarity measure (TF-IDF)**: TF-IDF\
  \ vectors capture lexical overlap but not semantic meaning. For the similarity graph to capture discourse coherence, it\
  \ needs a similarity measure that identifies when two sentences are semantically related even if they share no words. Sentence\
  \ embeddings from pretrained language models (SBERT [13], InstructOR [14]) are designed for exactly this task. We were unable\
  \ to use SBERT in our experimental environment due to dependency constraints but identify this as the most critical improvement\
  \ for future work.\n\n3. **Missing rhetorical structure**: Human reading comprehension is guided not just by semantic similarity\
  \ but by *rhetorical relations* between sentences (e.g., elaboration, contrast, evidence). RST parsers can identify these\
  \ relations, and incorporating them as weighted edges would provide a graph that directly models discourse structure. This\
  \ is a key direction for future work.\n\n### 5.3 Comparison to Prior Work\n\nOur approach differs from prior graph-based\
  \ coherence models [8, 9] in its use of a global spectral graph property (effective resistance) rather than local graph\
  \ features. However, the current results do not establish that effective resistance is superior to local features—indeed,\
  \ we have not yet performed a direct comparison on the same benchmark.\n\nCompared to deep learning approaches [6], our\
  \ method has the advantage of interpretability but lower accuracy on the CLEAR benchmark. A hybrid approach combining effective\
  \ resistance features with neural architectures is a promising direction.\n\n### 5.4 Future Directions\n\nSeveral avenues\
  \ for future research emerge:\n\n1. **Neural sentence embeddings for graph construction**: Replacing TF-IDF with SBERT embeddings\
  \ for similarity computation. This would allow the graph to capture semantic relatedness beyond lexical overlap.\n\n2. **RST-based\
  \ graph construction**: Using discourse parsers to identify rhetorical relations and incorporating them as edges. Initial\
  \ work could use rule-based discourse segmenters if full RST parsers are unavailable.\n\n3. **Evaluation on additional benchmarks**:\
  \ The CLEAR corpus is one of several readability datasets with human judgments. Evaluating on WeeBit [15], OneStopEnglish\
  \ [16], and the Newsela dataset would establish the method's generalizability (or lack thereof).\n\n4. **Cognitive validation**:\
  \ Collecting eye-tracking data to validate whether effective resistance predicts reading times and comprehension would provide\
  \ strong evidence for the cognitive plausibility of the metric.\n\n5. **Approximation algorithms**: For very long documents\
  \ (>1000 sentences), exact computation of the pseudoinverse may be prohibitively expensive. Recent work on fast estimation\
  \ of Laplacian pseudoinverse diagonal entries [17] could enable efficient approximation.\n\n6. **Hybrid models**: Combining\
  \ effective resistance with traditional surface features and neural embeddings in a fusion model could leverage the strengths\
  \ of each approach. The effective resistance feature may capture complementary signal when computed from rich discourse\
  \ graphs.\n\n\n## 6 Conclusion\n\nWe have introduced a novel readability metric based on the effective electrical resistance\
  \ of discourse graphs. By modeling text as an electrical circuit where sentences are connected by semantic pathways, the\
  \ Kirchhoff index provides a physically-motivated, interpretable measure of readability that captures discourse-level coherence\
  \ beyond surface features.\n\nHonest evaluation on the CLEAR corpus (N=4,724 real human judgments) reveals that the current\
  \ implementation does not outperform traditional readability formulas. The sequential graph construction reduces to measuring\
  \ sentence count, and the TF-IDF similarity graph construction achieves low correlation (r=0.12) with human judgments. Traditional\
  \ formulas (Flesch-Kincaid: r=0.50, SMOG: r=0.55) remain substantially more accurate.\n\nThese negative results are informative.\
  \ They identify specific failure modes—degenerate graph construction, insufficient similarity measures, and missing rhetorical\
  \ structure—and point to concrete improvements: using neural sentence embeddings (SBERT) for similarity computation and\
  \ RST parsers for discourse relation edges. We hope our honest reporting of these results accelerates progress by clarifying\
  \ what does and does not work in applying electrical network theory to readability assessment.\n\nMore broadly, this work\
  \ demonstrates the value of rigorous evaluation on established benchmarks with real human judgments. Initial promising results\
  \ on synthetic data (r=0.80) did not generalize to real data—a reminder that readability assessment requires evaluation\
  \ on diverse, naturalistic texts with genuine human annotations.\n\n## Acknowledgments\n\nWe thank the CommonLit organization\
  \ for making the CLEAR corpus publicly available, and the anonymous reviewers for their incisive critiques that substantially\
  \ improved this paper.\n\n## References\n\n[1] Mesgar, M., \\& Strube, M. (2015). Graph-based Coherence Modeling For Assessing\
  \ Readability. In *Proceedings of the Fourth Joint Conference on Lexical and Computational Semantics* (pp. 309-318).\n\n\
  [2] Flesch, R. (1948). A new readability yardstick. *Journal of Applied Psychology*, 32(3), 221-233.\n\n[3] McLaughlin,\
  \ G. H. (1969). SMOG grading: A new readability formula. *Journal of Reading*, 12(8), 639-646.\n\n[4] Coleman, M., \\& Liau,\
  \ T. L. (1975). A computer readability formula designed for machine scoring. *Journal of Applied Psychology*, 60(2), 283-284.\n\
  \n[5] Klein, K. G., et al. (2025). Readability Formulas, Systems and LLMs are Poor Predictors of Reading Ease. In *Proceedings\
  \ of the Conference on Empirical Methods in Natural Language Processing*. arXiv:2502.11150.\n\n[6] Zhang, L., et al. (2026).\
  \ Automatic text readability assessment for educational content based on graph representation learning. *Scientific Reports*,\
  \ 16, 11308.\n\n[7] Kincaid, J. P., et al. (1975). Derivation of new readability formulas (Automated Readability Index,\
  \ Fog Count and Flesch Reading Ease Formula) for Navy enlisted personnel. Naval Technical Training Command.\n\n[8] Mesgar,\
  \ M., \\& Strube, M. (2015). Graph-based Coherence Modeling For Assessing Readability. In *Proceedings of the Fourth Joint\
  \ Conference on Lexical and Computational Semantics*.\n\n[9] Guinaudeau, C., \\& Strube, M. (2013). Graph-based Local Coherence\
  \ Modeling. In *Proceedings of the 51st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long\
  \ Papers)* (pp. 93-103).\n\n[10] Ehret, K. (2018). Kolmogorov complexity as a universal measure of language complexity.\
  \ In *Proceedings of the Meeting of the Linguistic Association of Canada and the United States*.\n\n[11] Ellens, W., et\
  \ al. (2011). Effective graph resistance. *Linear Algebra and its Applications*, 435(10), 2491-2506.\n\n[12] Crossley, S.,\
  \ et al. (2021). The CommonLit Ease of Readability (CLEAR) Corpus. *Behavior Research Methods*, 53(4), 1583-1599.\n\n[13]\
  \ Reimers, N., \\& Gurevych, I. (2019). Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks. In *Proceedings\
  \ of the 2019 Conference on Empirical Methods in Natural Language Processing*.\n\n[14] Su, H., et al. (2023). One Embedder,\
  \ Any Task: Instruction-Finetuned Text Embeddings. *Findings of ACL 2023*.\n\n[15] Deutsch, T., Jasbi, M., \\& Shieber,\
  \ S. (2020). Linguistic Features for Readability Assessment. arXiv:2006.00377.\n\n[16] Vajjala, S., \\& Lucic, I. (2018).\
  \ OneStopEnglish corpus: A new corpus for automatic readability assessment and text simplification. In *Proceedings of the\
  \ Workshop on Automatic Text Simplification* (pp. 297-304).\n\n[17] Lu, Z., Xu, W., \\& Zhang, Z. (2023). Diagonal of Pseudoinverse\
  \ of Graph Laplacian: Fast Estimation and Exact Results. arXiv:2310.05527.\n"
summary: >-
  We propose a novel readability metric based on effective electrical resistance of discourse graphs. Honest evaluation on
  the CLEAR corpus (N=4,724 real human judgments) shows the sequential graph construction reduces to sentence count (r=0.32,
  same as sentence count) and similarity-based graph construction achieves low correlation (r=0.12). Traditional formulas
  (Flesch-Kincaid: r=0.50, SMOG: r=0.55) substantially outperform our method. We identify specific failure modes and outline
  concrete improvements for future work: neural sentence embeddings and RST-based graph construction.
</paper_text>

<available_figures>
--- Item 1 ---
id: fig1
title: 'Scatter Plot: Sequential Graph ER vs Human Judgments'
caption: >-
  Scatter plot of Sequential Graph Effective Resistance scores versus human readability judgments on the CLEAR corpus (N=4,724).
  Scores cluster into discrete bands corresponding to sentence counts, illustrating that the sequential graph method reduces
  to measuring sentence count.
image_gen_detailed_description: >-
  Scatter plot with 4724 points. X-axis: Sequential Graph ER score (normalized, range -0.011 to -0.003). Y-axis: Human readability
  judgment (1-100). Points form discrete vertical bands at 39 distinct x-values, each band corresponding to a specific sentence
  count (2-41 sentences). Trend line is step-like rather than continuous. Axes labeled clearly. Sans-serif font, white background.
aspect_ratio: '21:9'
summary: Shows that sequential graph ER reduces to sentence count
figure_path: figures/fig1_v0.jpg

--- Item 2 ---
id: fig2
title: Correlation Comparison Across Methods
caption: >-
  Pearson correlation coefficients for all evaluated readability metrics on the CLEAR corpus. Traditional formulas (Flesch-Kincaid:
  r=0.50, SMOG: r=0.55, Coleman-Liau: r=0.48) substantially outperform the effective resistance methods (Sequential Graph:
  r=0.32, TF-IDF Similarity Graph: r=0.12).
image_gen_detailed_description: >-
  Grouped bar chart. X-axis: Method names (6 methods). Y-axis: Pearson correlation r (0.0 to 0.6). Values: Sequential Graph
  ER=0.32 (blue bar), TF-IDF Similarity Graph ER=0.12 (blue bar), Flesch-Kincaid=0.50 (orange bar), SMOG=0.55 (orange bar),
  Coleman-Liau=0.48 (orange bar), Sentence Count=0.32 (gray bar). Error bars not shown (values are exact correlations). Sans-serif
  font, white background.
aspect_ratio: '21:9'
summary: Compares correlation across all methods
figure_path: figures/fig2_v0.jpg

--- Item 3 ---
id: fig3
title: Runtime Scaling with Document Length
caption: >-
  Runtime for effective resistance computation as a function of the number of sentences. Runtime remains under 10 ms even
  for the longest documents (41 sentences), confirming computational feasibility for real-time applications.
image_gen_detailed_description: >-
  Line plot. X-axis: Number of sentences (2 to 41). Y-axis: Runtime in milliseconds (0 to 10). Points at: (2, 0.2ms), (5,
  0.5ms), (10, 1.1ms), (20, 3.2ms), (30, 6.1ms), (41, 8.7ms). Line shows sub-linear growth. Sans-serif font, white background.
aspect_ratio: '21:9'
summary: Shows runtime scaling is feasible
figure_path: figures/fig3_v0.jpg
</available_figures>

<figure_requirements>
CRITICAL: Include ALL figures from <available_figures>. No exceptions.

- Every figure MUST use \includegraphics{figures/filename.jpg}
- Do NOT skip, convert to tables, or describe without inserting
- Each needs: \begin{figure*|figure}[placement], \includegraphics, \caption, \label, \end{...} — pick env + placement by the figure's `aspect_ratio` field (see PLACEMENT below). Constrain every \includegraphics with `width=\linewidth,height=0.4\textheight,keepaspectratio` (single-column) or `width=\textwidth,height=0.45\textheight,keepaspectratio` (figure*). Use exactly these option keys — `max height=` is NOT valid LaTeX
- Use the `caption` field from each figure for \caption{...} — do NOT invent new captions
- Place figures where their [FIGURE:fig_id] markers appear in paper_text
- VERIFICATION: paper.tex MUST have exact same number of \includegraphics as <available_figures>
- Do NOT generate new figure images (no matplotlib, no PIL, no image generation). Use ONLY the pre-generated figures from <available_figures>. They were already created by a previous pipeline step.

PLACEMENT BY ASPECT RATIO (use the `aspect_ratio` field on each figure):
- `21:9` (architecture diagrams / hero figures): \begin{figure*}[!t] (full two-column width, top of page). The hero architecture diagram should appear EARLY in the paper — typically at the top of page 2. Marker placement in paper_text already determines this; preserve it.
- `16:9` (comparisons, multi-panel results): \begin{figure*}[!t] for full-width or \begin{figure}[!htbp] for single-column.
- `4:3` / `1:1` / `3:2` / `3:4` / `9:16`: \begin{figure}[!htbp] (single-column).
</figure_requirements>

<artifact_links>
The paper_text contains \footnote{Code: \url{...}} references linking to artifact source code
on GitHub. Include \usepackage{hyperref} and \usepackage{url}.
Preserve these exactly as-is — do not remove, rewrite, or convert them to plain text.
The URLs will not resolve yet (the repo is deployed after compilation) — do NOT try to verify or fix them.
</artifact_links>

<headings>
NEVER use inline math (``$...$``) inside ``\section{...}`` / ``\subsection{...}`` / ``\subsubsection{...}`` arguments — hyperref's bookmark builder errors out (``Token not allowed in a PDF string``) and the PDF outline breaks. If a section heading needs a math-looking term, use the text equivalent (``d star`` not ``$d^*$``, ``alpha-equivalent`` not ``$\alpha$-equivalent``) or wrap it in ``\texorpdfstring{$math$}{plain}``. Inline math inside body paragraphs is fine.
</headings>

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-paper-to-latex, aii-semscholar-bib.
TODO 2. Review <paper_text> and <available_figures>. Copy all figure images into ./figures/ in your workspace. Count figures — MUST include every one. Plan placements per section. Build `./references.bib` via aii_semscholar_bib__fetch — collect DOIs/ArXiv IDs from <paper_text> and batch-fetch all BibTeX in one call. Do NOT fabricate entries.
TODO 3. Create `./paper.tex` per aii-paper-to-latex skill's setup, write ALL sections, insert ALL figures from <available_figures>, include `./references.bib` via \bibliography. Compile to PDF per skill's process. Fix errors.
TODO 4. CRITICAL VERIFICATION: Run `grep -c 'includegraphics' paper.tex`, confirm count equals figures in <available_figures>. If not, add missing figures. Verify `./paper.pdf` was created.
TODO 5. VISUAL REVIEW: Write Python script to convert EVERY page of paper.pdf to PNG at 150 DPI (use pdf2image or pymupdf). Then read ALL page screenshots — each page image costs ~1,600 tokens so a 15-page paper is only ~24K tokens. You MUST read every page. The ONLY exception is if all page images would not fit in your remaining context — in that case, read as many as fit and state which pages you are skipping and why. Check every page for layout issues, overlapping figures, cut-off text, bad spacing, formatting problems. Fix issues and recompile.
TODO 6. FINAL READ: Check page count (`pdfinfo paper.pdf` or pymupdf). Read entire paper.pdf — check for missing sections, unclear explanations, inconsistencies, typos. Fix and recompile. The ONLY exception is if all pages would not fit in your remaining context — in that case, read as many pages as fit and state which pages you are skipping and why.
</todos>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_RiHQW43yNEvO/4_gen_paper_repo/_4_assemble_paper/paper/workspace/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "FullPaperExpectedFiles": {
      "description": "All expected output files from full paper generation.",
      "properties": {
        "paper_tex_path": {
          "description": "Path to LaTeX source file. Example: 'paper.tex'",
          "title": "Paper Tex Path",
          "type": "string"
        },
        "paper_pdf_path": {
          "description": "Path to compiled PDF. Example: 'paper.pdf'",
          "title": "Paper Pdf Path",
          "type": "string"
        },
        "references_bib_path": {
          "description": "Path to BibTeX bibliography file. Example: 'references.bib'",
          "title": "References Bib Path",
          "type": "string"
        },
        "figure_paths": {
          "description": "Paths to all figure image files. Example: ['figures/fig1_v0.jpg', 'figures/fig2_v0.jpg']",
          "items": {
            "type": "string"
          },
          "title": "Figure Paths",
          "type": "array"
        }
      },
      "required": [
        "paper_tex_path",
        "paper_pdf_path",
        "references_bib_path",
        "figure_paths"
      ],
      "title": "FullPaperExpectedFiles",
      "type": "object"
    }
  },
  "description": "Full paper \u2014 structured output from paper generation.",
  "properties": {
    "title": {
      "description": "Paper title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance. Aim for about 4-8 words (~40 characters).",
      "maxLength": 90,
      "minLength": 12,
      "title": "Title",
      "type": "string"
    },
    "summary": {
      "description": "Brief summary of the generated paper: sections written, figures included, compilation status",
      "maxLength": 5000,
      "minLength": 500,
      "title": "Summary",
      "type": "string"
    },
    "out_expected_files": {
      "$ref": "#/$defs/FullPaperExpectedFiles",
      "description": "All output files you created. Must include paper.tex, paper.pdf, references.bib, and paths to all figure files."
    }
  },
  "required": [
    "title",
    "summary",
    "out_expected_files"
  ],
  "title": "FullPaper",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `/ai-inventor/aii_data/runs/run_RiHQW43yNEvO/4_gen_paper_repo/_4_assemble_paper/paper/workspace/.sdk_openhands_agent_struct_out.json`.
````

### [2] HUMAN-USER prompt · 2026-07-08 12:57:28 UTC

```
Propose a simple, novel, testable ML method for scoring text readability and validate it with a tiny experiment.
```

### [3] SKILL-INPUT — aii-paper-to-latex · 2026-07-08 12:57:47 UTC

The agent loaded the **aii-paper-to-latex** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-paper-to-latex
description: LaTeX paper assembly and compilation. Covers document setup, figure inclusion from pre-generated JPEGs, compilation process, and output files. Use when assembling a paper from pre-written text and pre-generated figures into a compiled PDF.
---

## LaTeX Paper Assembly

Assembles a research paper from paper text, pre-generated figure JPEGs, and bibliography into a compiled PDF.

### Document Setup

```latex
\documentclass[11pt,letterpaper]{article}
\usepackage{graphicx, geometry, amsmath, hyperref, natbib, booktabs, xcolor, listings}
\geometry{margin=1in}
\hypersetup{colorlinks=true, linkcolor=black, citecolor=black, urlcolor=black}
```

### Figure Inclusion

CRITICAL: Include ALL figures. Every figure MUST appear in the paper.

```latex
\begin{figure}[!htbp]
  \centering
  \includegraphics[width=0.92\textwidth,keepaspectratio]{figures/filename.jpg}
  \caption{Descriptive caption.}
  \label{fig:label}
\end{figure}
```

Rules:
- ALWAYS use `[!htbp]` float placement (NOT `[t]` or `[h]` alone)
- ALWAYS constrain with `width` and `keepaspectratio` to prevent page takeover
- Every figure needs `\caption`, `\label`, and a `\ref` in the text
- Do NOT convert figures to tables or describe them without inserting the image
- Do NOT skip any figures

### Compilation Process

Run each command separately (do NOT chain with `&&` — pdflatex often exits non-zero on warnings, which would skip bibtex and leave citations as `??`):

```bash
pdflatex -interaction=nonstopmode paper.tex
bibtex paper
pdflatex -interaction=nonstopmode paper.tex
pdflatex -interaction=nonstopmode paper.tex
```

All four commands are required. Skipping bibtex causes `??` in all citations.
Fix any errors between runs. Verify `./paper.pdf` was created.

### Output Files

- `./paper.tex` — LaTeX source
- `./references.bib` — bibliography file
- `./paper.pdf` — compiled PDF
- `./figures/*.jpg` — all figure images (pre-generated, copied into workspace)
````

### [4] SKILL-INPUT — aii-semscholar-bib · 2026-07-08 12:57:47 UTC

The agent loaded the **aii-semscholar-bib** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-semscholar-bib
description: Build bibliographies using Semantic Scholar. Batch-fetch BibTeX for papers by DOI, ArXiv ID, or title. Use when writing papers, generating reference lists, or building .bib files.
---

## Tool: `aii_semscholar_bib__fetch`

Batch-fetch BibTeX entries from Semantic Scholar. Pass all references in a single call — the tool handles batching internally.

### How it works

1. **DOI/ArXiv refs** → batched into POST /paper/batch calls (up to 500 per API call, auto-chunked)
2. **Title-only refs** → individual GET /paper/search/match (1s delay between)
3. **Post-process** → fix entry type, fix citation key (AuthorYYYY), inject DOI

The ability server runs a single worker (`max_threads: 1`). Multiple concurrent tool calls are queued — each runs independently (no cross-request aggregation). Batching happens within each request.

### Input format

```json
{
  "references": [
    {"doi": "10.48550/arXiv.1706.03762", "author": "Vaswani", "year": 2017},
    {"arxiv": "2201.11903", "author": "Wei", "year": 2022},
    {"title": "Tree of Thoughts", "author": "Yao", "year": 2023}
  ]
}
```

Each reference object can have:
- `doi` — DOI string (ArXiv DOIs like `10.48550/arXiv.XXXX.XXXXX` auto-convert to ArXiv IDs)
- `arxiv` — ArXiv ID (e.g. `"2305.14325"`)
- `title` — Paper title (used for search/match when no DOI/ArXiv)
- `author` — First author last name (for cleaner citation key)
- `year` — Publication year (int, for citation key)

At least one of `doi`, `arxiv`, or `title` is required per reference.

### Output format

```json
{
  "success": true,
  "bib_text": "@inproceedings{Vaswani2017, ...}\n\n@article{Wei2022, ...}",
  "total": 3,
  "found": 3,
  "failed_count": 0,
  "entries": [{"citation_key": "Vaswani2017", "bibtex": "...", "title": "...", "doi": "...", "arxiv": ""}],
  "failed": []
}
```

### Workflow

1. Collect DOIs, ArXiv IDs, or titles for all papers you need to cite
2. Call `aii_semscholar_bib__fetch` with the full list in **one call**
3. Save `bib_text` from the response to your `references.bib` file
4. Check `failed` — for any missed papers, follow the **fallback procedure** below

### Fallback for failed references (MANDATORY)

NEVER fabricate BibTeX. For each failed reference:
1. **WebSearch** for `"Title" author year` (try `site:arxiv.org` too)
2. **WebFetch** the paper page → extract title, authors, year, venue, DOI/ArXiv ID
3. If DOI/ArXiv found → retry `aii_semscholar_bib__fetch` with it
4. Last resort: write BibTeX by hand using **only verified info from the actual paper page**

---

### CLI (for manual use / debugging)

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-semscholar-bib" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_semscholar_bib__fetch.py --refs '[
  {"doi": "10.48550/arXiv.1706.03762", "author": "Vaswani", "year": 2017},
  {"arxiv": "2201.11903", "author": "Wei", "year": 2022},
  {"title": "Tree of Thoughts", "author": "Yao", "year": 2023}
]'
```

`--json, -j` — output raw JSON instead of .bib text

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````
