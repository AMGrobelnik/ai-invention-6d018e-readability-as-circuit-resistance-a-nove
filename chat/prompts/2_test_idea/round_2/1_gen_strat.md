# gen_strat_1 — test_idea

> Phase: `invention_loop` · round 2 · `gen_strat`
> Run: `run_RiHQW43yNEvO` — Simple Readability Score
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_strat_1` (sdk_openhands_agent)

### [1] SYSTEM-USER prompt · 2026-07-08 11:17:06 UTC

````
<hypothesis>
Your strategy should advance this hypothesis.

kind: hypothesis
title: Readability as Circuit Resistance
hypothesis: >-
  Text readability can be modeled through effective electrical resistance of discourse graphs with SEMANTIC edges between
  sentences. The Kirchhoff index of graphs where edges are weighted by semantic similarity (cosine distance between SBERT
  embeddings) provides a readability metric that captures discourse coherence beyond sentence count. Unlike sequential-only
  graphs (which reduce to sentence counting and produce trivially few distinct values), semantic edges enable the metric to
  capture meaningful variance in discourse structure. The first experiment using sequential edges and synthetic data with
  limited sentence counts (1-3 sentences) was invalid and must be repeated with rich discourse graphs and established benchmarks
  containing real human judgments.
motivation: >-
  Current readability formulas rely on surface features (sentence length, word difficulty) or black-box ML models that don't
  explicitly model the cognitive process of reading. Drawing from electrical network theory, we propose that readable text
  should allow 'easy information flow' through semantic connections, analogous to current flowing through a low-resistance
  circuit. This provides a theoretically grounded, interpretable metric that captures discourse-level coherence in a way surface
  features cannot.
assumptions:
- >-
  Text can be meaningfully represented as a graph where sentences are nodes and edges represent discourse connections (semantic
  similarity, rhetorical relations, or sequential adjacency)
- >-
  The cognitive effort of reading correlates with the 'resistance' to information flow through the discourse graph
- >-
  Edge weights (resistances) can be meaningfully assigned based on semantic distance or discourse relation strength
- >-
  The effective graph resistance (Kirchhoff index) computed from this weighted graph correlates with human judgments of readability
investigation_approach: >-
  1. Construct discourse graphs from texts: nodes=sentences, edges=semantic connections weighted by cosine distance between
  sentence embeddings (or simplified: sequential edges with weights based on position). 2. Compute the effective graph resistance
  (trace of Laplacian pseudoinverse) as the readability score. 3. Evaluate on standard readability datasets (e.g., Weebit,
  CLEAR) by correlating with human ratings. 4. Compare against traditional formulas (Flesch-Kincaid, SMOG) and ML baselines.
  5. Perform ablation: test different graph construction methods (sequential only, similarity-thresholded, full RST parsing).
success_criteria: >-
  The effective resistance metric should: (1) Achieve Pearson correlation r > 0.7 with human readability ratings on standard
  benchmarks, (2) Outperform or match traditional readability formulas (Flesch-Kincaid, etc.) in predictive accuracy, (3)
  Show significant correlation (p < 0.01) with reading time/eye-tracking measures if available, (4) Be computationally feasible
  (< 1s per document for typical lengths). A tiny experiment (N=50 texts with human ratings) showing r > 0.5 would support
  proceeding to full evaluation.
related_works:
- >-
  Mesgar & Strube (2015) 'Graph-based Coherence Modeling For Assessing Readability' - Uses entity grids and discourse relation
  graphs with features like outdegree and frequent subgraphs, but does NOT use effective resistance. Our approach differs
  by using the actual electrical network resistance as the direct readability metric, which captures global information flow
  rather than local graph patterns.
- >-
  Zhang et al. (2026) 'Automatic text readability assessment for educational content based on graph representation learning'
  - Uses GCNs on POS-based dependency graphs. This is a deep learning approach that learns features implicitly, whereas our
  method uses a specific, interpretable graph metric (effective resistance) derived from network theory.
- >-
  Guinaudeau & Strube (2013) 'Graph-based coherence modeling' - Introduces entity graphs and one-mode projections for coherence
  modeling. Our work differs by using effective resistance (a global spectral graph property) rather than local features like
  edge weights or components.
- >-
  Ehret (2018) 'Kolmogorov complexity as a universal measure of language complexity' - Uses compression-based complexity.
  While both approaches use information theory concepts, effective resistance captures discourse-level connectivity while
  Kolmogorov complexity captures lexical/syntactic redundancy.
- >-
  Klein et al. (2025) 'Surprisal Takes It All: Eye Tracking Based Cognitive Evaluation of Text Readability Measures' - Finds
  surprisal (from language models) predicts reading ease. Our approach is complementary: effective resistance models discourse
  structure while surprisal models lexical predictability.
inspiration: >-
  The hypothesis draws from electrical network theory (Kirchhoff's laws, effective resistance) and its application to graph
  analysis. In electrical engineering, the effective resistance between nodes in a network captures how easily current can
  flow. We adapt this to text by treating discourse connections as electrical pathways: coherent, well-connected text has
  low 'resistance' to information flow, while disjointed or complex text has high resistance. This cross-domain transfer from
  circuit theory to readability assessment is, to our knowledge, novel.
terms:
- term: Effective resistance (Kirchhoff index)
  definition: >-
    The sum of resistance distances between all pairs of nodes in a graph, equivalent to the trace of the pseudoinverse of
    the graph Laplacian. In electrical networks, this represents the total resistance 'seen' by current flowing through the
    network.
- term: Graph Laplacian
  definition: >-
    A matrix representation of a graph L = D - A, where D is the degree matrix and A is the adjacency matrix. The pseudoinverse
    of L is used to compute effective resistances between nodes.
- term: Discourse graph
  definition: >-
    A graph representation of text where nodes represent sentences or discourse units, and edges represent rhetorical relations,
    semantic connections, or sequential adjacency.
- term: Resistance distance
  definition: >-
    A graph metric derived from electrical network theory that measures the effective electrical resistance between two nodes
    if unit resistors are placed on each edge. It captures both direct and indirect pathways between nodes.
- term: Kirchhoff index
  definition: >-
    The sum of all pairwise resistance distances in a graph. It is a global graph invariant that measures the overall 'connectivity'
    or 'flow capacity' of the network.
summary: >-
  We propose a novel readability metric based on effective electrical resistance of discourse graphs. By modeling text as
  a circuit where sentences are connected by semantic pathways, the total resistance to information flow (Kirchhoff index)
  provides a physically-motivated, interpretable measure of readability that captures discourse-level coherence beyond surface
  features.
_relation_rationale: >-
  First experiment invalid (only 2 values); refining to require semantic edges, not just sequential.
_confidence_delta: decreased
_key_changes:
- >-
  Added REQUIREMENT for semantic edges (SBERT embeddings) instead of just sequential edges
- >-
  Acknowledged first experiment was invalid: only 2 distinct values, correlation = sentence count
- >-
  Added success criterion: metric must produce continuous range of values across diverse texts
- >-
  Added success criterion: partial correlation controlling for sentence count must remain significant
- >-
  Changed evaluation to use established benchmarks (CLEAR, WeeBit) with REAL human judgments
- >-
  Added ablation comparing sequential-only vs. semantic edges to quantify discourse contribution
- Emphasized edge weights must be based on semantic distance, not uniform
- Noted normalization scheme needs theoretical justification
relation_type: evolution
</hypothesis>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. Use it for study design, proper baselines, and the evaluation/validity norms this field demands.

- **aii-handbook-multi-llm-agents** — Guide for implementing Multi-LLM Agent Systems research using Mirascope orchestration, HuggingFace datasets/evaluation, and proven multi-agent patterns.
</available_domain_handbooks>

<iteration_status>
Current iteration: 2 of 2
Remaining (including this one): 1
</iteration_status>

<previous_strategies>
Strategies from the PREVIOUS iteration. You can CONTINUE these directions,
ADAPT based on what worked and what didn't in the artifacts produced, or PIVOT if results suggest a better path.

--- Strategy 1 ---
kind: strategy
id: gen_strat_1_idx1
title: Test readability as circuit resistance hypothesis
objective: >-
  Validate whether effective electrical resistance of discourse graphs correlates with human readability judgments through
  initial implementation and tiny-scale experiment
rationale: >-
  This is a novel, physically-motivated readability metric that captures discourse-level coherence beyond surface features.
  Iteration 1 establishes the computation method and runs a preliminary correlation analysis. The dataset artifact ensures
  standardized data is available for iteration 2's full evaluation.
artifact_directions:
- id: research_iter1_dir1
  type: research
  objective: >-
    Research effective resistance computation and discourse graph construction methods for readability assessment
  approach: >-
    Conduct web research on: (1) Computing Kirchhoff index / effective resistance from graph Laplacian pseudoinverse - search
    for Python implementations and numerical stability considerations, (2) Discourse graph construction approaches - sequential
    edges vs semantic similarity edges vs RST-based edges, weighting schemes, (3) Available readability benchmark datasets
    (Weebit, CLEAR, Newsela) - their size, format, and how to access them. Summarize findings in a structured report with
    implementation recommendations.
  depends_on: []
- id: dataset_iter1_dir2
  type: dataset
  objective: >-
    Acquire and standardize a readability dataset with human judgments for experiment validation
  approach: >-
    Search HuggingFace Hub and direct academic sources for readability datasets. Prioritize: (1) Weebit dataset (550 texts,
    human ratings), (2) CLEAR dataset, (3) any dataset with text passages + human readability scores. Download, standardize
    to JSON format with fields: text, sentence_boundaries, readability_score (normalized 0-1 or 1-100), text_id, metadata.
    Create full/mini/preview splits. If Weebit not available, try alternative sources or construct a small dataset from Project
    Gutenberg books with known reading levels.
  depends_on: []
- id: experiment_iter1_dir3
  type: experiment
  objective: >-
    Implement effective resistance readability metric and compute preliminary correlation on a tiny test set
  approach: >-
    Implement the effective resistance metric: (1) Sentence segmentation using NLTK/ spaCy, (2) Sentence embeddings using
    sentence-transformers (all-MiniLM-L6-v2), (3) Build discourse graph: nodes=sentences, edges=semantic connections weighted
    by 1/(1+cosine_similarity) as resistance, (4) Compute graph Laplacian L = D - A, (5) Compute pseudoinverse L^+ using scipy.linalg.pinv,
    (6) Kirchhoff index = trace(L^+) * n_nodes (or sum of all pairwise resistance distances). For tiny validation: download
    20-30 texts with known reading levels (Gutenberg) or use built-in sklearn text data. Compute correlation with baseline
    metrics (Flesch-Kincaid via textstat). Output: correlation coefficients, p-values, runtime per document.
  depends_on: []
expected_outcome: >-
  By end of iteration 1: (1) Research report documenting effective resistance computation approach, (2) Standardized readability
  dataset (Weebit or alternative) in JSON format ready for iteration 2, (3) Preliminary experimental results showing whether
  the effective resistance metric produces sensible readability scores and initial correlation with reading level. This establishes
  proof-of-concept for iteration 2's full evaluation.
summary: >-
  First iteration establishes methodology (research), acquires evaluation data (dataset), and implements the novel metric
  with tiny-scale validation (experiment). This lays the groundwork for full correlation analysis against human judgments
  in iteration 2.
</previous_strategies>

<dependency_rules>
- depends_on is a list of objects {id, label} — each entry references an existing artifact and tags how it is being used
- "id" can ONLY reference IDs from <existing_artifacts> — never IDs you are proposing (all new artifacts run in parallel)
- "label" is a SHORT free-text type label (a word or two, NOT a sentence) describing what role the dep plays — e.g. "dataset", "validates", "extends", "supersedes". Required on every dep.
- Setting depends_on provides the dependency's out_dependency_files to your artifact at execution time
- If no suitable existing artifacts exist, use empty depends_on
- New artifact IDs are assigned by the system after submission — do not invent IDs for your proposed artifacts
</dependency_rules>

<available_artifact_types>
Artifact types you can plan. Use this to choose the right types for your strategy objectives.

<artifact_types>
RESEARCH
Web research to answer key questions — like a researcher making decisions.
Runtime: LLM Agent, no code execution.
Tools: the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text).
Capabilities: Find, synthesize, and compare information across sources; survey SOTA and best practices.
Deps: REQUIRED none | OPTIONAL other RESEARCH to build on prior findings

EXPERIMENT
Run code to test hypotheses, implement methods, and collect empirical results.
Runtime: Python 3.12, UV (any pip package), isolated workspace, gradual scaling (mini → full data).
Tools: Full shell/Python/filesystem access, the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text), and other skills.
Skills: aii-json (schema validation), aii-openrouter-llms (call any LLM — GPT, Gemini, Llama, etc.), domain-specific as needed.
Capabilities: Implement and run any code-based experiment, compare method vs baselines.
Deps: REQUIRED at least one DATASET | OPTIONAL RESEARCH for methodology guidance

DATASET
Collect, prepare, and merge datasets for experiments and analysis.
Runtime: Python 3.12, UV, isolated workspace.
Tools: Full shell/Python/filesystem access, the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text), and other skills.
Skills: aii-hf-datasets (HuggingFace Hub — ML datasets, many UCI/OpenML/Kaggle mirrors), aii-owid-datasets (Our World in Data — global statistics), aii-json (schema validation). Also any Python source (sklearn.datasets, openml, direct URLs, APIs) — must verify within 300MB limit.
Capabilities: Search, acquire, transform, combine, and standardize data from any available source.
Deps: REQUIRED none | OPTIONAL RESEARCH for guidance on what data to collect

EVALUATION
Evaluate experiment results with metrics, statistical analysis, and validity checks.
Runtime: Python 3.12, UV (any evaluation library), isolated workspace, gradual scaling matching experiment.
Tools: Full shell/Python/filesystem access, the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text), and other skills.
Skills: aii-json (schema validation), aii-openrouter-llms (call any LLM — GPT, Gemini, Llama, etc.), domain-specific as needed.
Capabilities: Compute any quantitative metrics and statistical tests, analyze validity and robustness.
Deps: REQUIRED at least one EXPERIMENT | OPTIONAL DATASET if reference data needed

PROOF
Formally prove mathematical statements in Lean 4 with automated iteration.
Runtime: LLM agent with Lean 4 compiler feedback loop.
Tools: Full shell/Python/filesystem access, the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text), and other skills.
Skills: aii-lean (proof verification, Mathlib search, tactics: ring, linarith, nlinarith, omega, simp, etc.)
Capabilities: Formally verify properties and inequalities, iterative proof development, lemma decomposition.
Deps: REQUIRED none | OPTIONAL RESEARCH for mathematical background
</artifact_types>
</available_artifact_types>

<artifact_executor_scope>
IMPORTANT: Each artifact executor has a focused prompt that guides it to do ONE thing well. It will NOT perform tasks outside its scope — assigning the wrong work to the wrong artifact type wastes an iteration. Match the task to the right executor.

RESEARCH executor scope:
  Output: research_out.json with {answer, sources, follow_up_questions} + research_report.md
  DOES: Web research — search, read, synthesize information from papers/docs/APIs into a structured report
  DOES NOT: Run code, download files, execute scripts, compute anything — no shell/Python access
  Use for literature surveys, API documentation, technical specifications — pure information gathering

EXPERIMENT executor scope:
  Output: method_out.json with results (metrics, predictions, analysis) — the core computational work
  DOES: Implement and run methods/algorithms, compute metrics, compare approaches, produce quantitative results
  DOES NOT: Collect new datasets (depends on DATASET artifacts for input data), write formal proofs
  This is the right artifact for any code that processes data and produces results

DATASET executor scope:
  Output: data_out.json with rows of {input, output, metadata_fold, ...} — raw data only, no derived computations
  DOES: Download/generate datasets, analyze candidates to pick the best ones, standardize to JSON schema (features, labels, folds, metadata), validate schema, split into full/mini/preview
  DOES NOT: Run experiments, train models, compute derived statistics (PID/MI/correlations/synergy matrices) as final output
  If you need to COMPUTE something from data (synergy matrices, MI scores, timing benchmarks), use an EXPERIMENT artifact instead

EVALUATION executor scope:
  Output: eval_out.json with evaluation results
  DOES: Any evaluation of experiment results — metrics, statistical tests, ablations, comparisons, visualizations, robustness checks, error analysis, etc.
  DOES NOT: Implement new methods (use EXPERIMENT), collect data (use DATASET)
  This is for analyzing experiment outputs from any angle

PROOF executor scope:
  Output: Lean 4 proof files (.lean) with verified theorems
  DOES: Write and verify Lean 4 formal proofs with Mathlib, iterative compilation
  DOES NOT: Run Python experiments, collect data, do empirical analysis
  Use only when formal mathematical guarantees are needed
</artifact_executor_scope>

<artifact_planning_rules>
RESEARCH: Plan early — findings guide dataset selection, experiment design, and methodology.
EXPERIMENT: Must depend on at least one DATASET. Define clear metrics and baselines before running. Consider trying multiple method variations rather than a single approach.
DATASET:
- Plan for REAL third-party datasets (HuggingFace, Kaggle, direct-download URLs) — downloadable within time and size constraints
- Describe dataset criteria (domain, size, format) — executors find exact sources, but you can suggest candidates or search directions
- ALWAYS prefer real datasets over synthetic. Synthetic is a LAST RESORT only when no suitable real data exists
EVALUATION: Must depend on at least one EXPERIMENT. Focus on statistical rigor and validity checks.
PROOF: Use only when the hypothesis requires formal mathematical guarantees. Lean 4 + Mathlib.
</artifact_planning_rules>

<existing_artifacts>
--- Item 1 ---
id: art_IM3J27ltI7Pm
type: research
title: Effective Resistance for Readability Graphs Research
summary: >-
  This research artifact provides comprehensive findings on three foundational components for implementing a 'Readability
  as Circuit Resistance' metric: (1) Computing effective resistance (Kirchhoff index) from graph Laplacian pseudoinverse -
  identified NetworkX built-in functions (resistance_distance, effective_graph_resistance) and netneurotools library with
  implementation code examples and numerical stability considerations. (2) Constructing discourse graphs from text - documented
  three edge construction methods (sequential, similarity-based with SBERT, RST-based), edge weighting schemes, and relevant
  Python libraries (sentence-transformers, NetworkX, RST parsers). (3) Identifying readability benchmark datasets - compiled
  detailed comparison of 5 datasets (WeeBit, CLEAR, Newsela, OneStopEnglish, Wikilarge) with sizes, rating scales, access
  methods, and licensing information. The artifact includes an implementation roadmap with specific library recommendations,
  sample code for computing resistance scores from text, and an evaluation plan using the CLEAR corpus. Confidence levels
  are assessed for each finding, and follow-up research questions are provided.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_RiHQW43yNEvO/3_invention_loop/iter_1/gen_art/gen_art_research_1
out_expected_files:
- research_out.json
out_dependency_files:
  file_list:
  - research_out.json

--- Item 2 ---
id: art_vYMmBxe-2BfW
type: dataset
title: Readability datasets for ML scoring
summary: >-
  Successfully collected 4 readability datasets from HuggingFace Hub, evaluated their provenance via web research, and selected
  the 2 best datasets for the experiment. The selected datasets are: 1) SetFit/onestop_english (567 examples, 3-class classification:
  Elementary/Intermediate/Advance) - an established benchmark with published paper (Vajala and Lučić, 2018), and 2) agentlans/readability
  (104,761 examples, regression with continuous grade scores 0-20) - diverse text sources including Wikipedia, ArXiv, and
  Fineweb-Edu. Both datasets were standardized to exp_sel_data_out.json schema with input (text), output (readability label/score),
  and metadata fields (fold, task_type, etc.). The full dataset (119MB) was split into 2 parts under 100MB each as required.
  All outputs validated against schema and preview/mini versions generated.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_RiHQW43yNEvO/3_invention_loop/iter_1/gen_art/gen_art_dataset_1
out_expected_files:
- data.py
- full_data_out.json
- preview_data_out.json
- mini_data_out.json
out_dependency_files:
  file_list:
  - data.py
  - full_data_out/full_data_out_1.json
  - full_data_out/full_data_out_2.json
  - mini_data_out.json
  - preview_data_out.json
  data_file_paths:
  - full_data_out/full_data_out_1.json
  - full_data_out/full_data_out_2.json
  - mini_data_out.json
  - preview_data_out.json

--- Item 3 ---
id: art_rfw45zxdqTLX
type: experiment
title: Circuit Resistance Readability Test
summary: >-
  Implemented and evaluated a novel effective resistance metric for text readability using discourse graphs. The method constructs
  a graph where sentences are nodes and edges represent discourse connections (sequential in this implementation). The Kirchhoff
  index (sum of effective resistances between all node pairs) serves as the readability score. Evaluated on 50 synthetic texts
  with known readability levels (simple/medium/complex). Results show strong correlation with human readability scores (Pearson
  r=0.80, Spearman ρ=0.81, p<0.001) and competitive performance with baseline metrics (Flesch-Kincaid r=0.87, SMOG r=0.85).
  The method is computationally efficient (0.004s per document) and provides a theoretically grounded alternative to traditional
  readability formulas. Limitations: current implementation uses sequential graphs only (no semantic similarity edges) due
  to environment constraints; future work should incorporate sentence embeddings for enhanced performance.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_RiHQW43yNEvO/3_invention_loop/iter_1/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json
out_dependency_files:
  file_list:
  - method.py
  - full_method_out.json
  - mini_method_out.json
  - preview_method_out.json
</existing_artifacts>

<current_paper>
The current paper draft — represents the research story so far.

Use this to understand what's working, what's not, and what gaps remain.
Gaps and weak results signal what to try differently — not what to conclude.

# Readability as Circuit Resistance: A Novel Physically-Motivated Metric Using Effective Graph Resistance

## Abstract

Traditional readability formulas rely on surface-level features such as sentence length and word difficulty, while modern machine learning approaches operate as black boxes that do not explicitly model the cognitive process of reading. We propose a novel, physically-motivated readability metric based on effective electrical resistance of discourse graphs. By modeling text as an electrical circuit where sentences are nodes and discourse connections are resistors, the total effective resistance (Kirchhoff index) of the graph provides a theoretically grounded measure of readability that captures discourse-level coherence. We evaluate this approach on a dataset of 50 synthetically generated texts with known readability levels, comparing against traditional baselines including Flesch-Kincaid, SMOG, and Coleman-Liau. Results show that the effective resistance metric achieves strong correlation with human readability judgments (Pearson $r = 0.80$, Spearman $\rho = 0.81$, $p < 0.001$), competitive with traditional formulas. The method is computationally efficient (3.3 ms per document on average) and provides an interpretable, physics-inspired framework for readability assessment. We discuss limitations of the current sequential graph construction and outline future work incorporating semantic similarity edges.

**Keywords:** readability assessment, effective resistance, graph theory, discourse coherence, Kirchhoff index

## 1 Introduction

Assessing the readability of text is a fundamental problem in natural language processing with applications spanning education, content creation, and accessibility [1]. Traditional readability formulas such as Flesch-Kincaid [2], SMOG [3], and Coleman-Liau [4] have been used for decades, relying primarily on surface features: sentence length, word length, and syllable counts. While these formulas are simple and interpretable, they fail to capture deeper structural and coherence properties of text that influence reading comprehension.

Recent advances in machine learning have produced more accurate readability models using neural architectures [5]. However, these approaches typically function as black boxes, learning implicit features from data without providing interpretable insights into *why* a text is difficult or easy to read. This limits their utility in educational settings where explainability is important.

A critical missing element in existing approaches is an explicit model of the *cognitive process of reading*. When humans read, they construct a coherent mental representation of the text by connecting sentences and integrating information across discourse units. Texts with strong discourse coherence—where sentences are tightly connected through semantic relationships—are easier to comprehend because information flows smoothly between ideas. Conversely, disjointed or poorly structured text impedes comprehension because readers must work harder to bridge gaps between ideas.

We propose to model this "information flow" using concepts from electrical network theory. In electrical circuits, current flows easily through pathways with low resistance, while high-resistance pathways impede current flow. Analogously, we hypothesize that readable text creates "low-resistance pathways" for information flow through coherent discourse connections, while complex or incoherent text presents "high-resistance" to comprehension.

Specifically, we represent text as a graph where sentences are nodes and discourse connections are weighted edges (resistors). The *effective resistance* (also known as the Kirchhoff index) of this graph—a global graph invariant derived from the pseudoinverse of the Laplacian matrix—provides our readability score. Intuitively, graphs with many short, well-connected pathways between sentences have low effective resistance (easy information flow = readable), while graphs with sparse or long paths have high effective resistance (impeded flow = difficult).

Our main contributions are:

1. **A novel readability metric** based on effective electrical resistance of discourse graphs, providing a physically-motivated and interpretable alternative to traditional formulas.

2. **Empirical evaluation** on synthetic texts with known readability levels, demonstrating that the effective resistance metric achieves Pearson correlation $r = 0.80$ with human judgments, competitive with established baselines.

3. **Computational efficiency analysis** showing that the method requires only 3.3 ms per document on average, making it suitable for real-time applications.

4. **Open-source implementation** of the effective resistance readability scorer, enabling reproducibility and future research.

The remainder of this paper is organized as follows. Section 2 reviews related work in readability assessment and graph-based coherence modeling. Section 3 formalizes the effective resistance metric and describes our graph construction approach. Section 4 presents the experimental evaluation, and Section 5 discusses limitations and future directions. Section 6 concludes.

[ARTIFACT:art_rfw45zxdqTLX]

## 1.1 Conceptual Analogy

Figure 1 illustrates the core analogy behind our approach: just as current flows easily through low-resistance electrical circuits, information flows easily through well-connected discourse graphs. Readable text creates "low-resistance pathways" for information flow, while complex text creates "high-resistance" that impedes comprehension.

[FIGURE:fig1]

## 2 Related Work

### 2.1 Traditional Readability Formulas

Traditional readability assessment relies on surface-level linguistic features. The Flesch Reading Ease formula [2] computes a weighted combination of average sentence length and average word syllables. The Flesch-Kincaid Grade Level [6] adapts this for educational grade levels. The SMOG index [3] counts polysyllabic words, while the Coleman-Liau index [4] uses character-level features. These formulas are widely used due to their simplicity but have well-documented limitations: they assume linear relationships between features and comprehension, ignore discourse structure, and fail on texts with non-standard syntax [7].

### 2.2 Graph-Based Coherence Modeling

Recent work has applied graph theory to model textual coherence. Mesgar and Strube [8] propose graph-based coherence features for readability assessment, using entity grids and discourse relation graphs with features like outdegree and frequent subgraphs. However, their approach uses local graph patterns rather than global spectral properties. Guinaudeau and Strube [9] introduce entity graphs and one-mode projections for coherence modeling, but similarly focus on local edge statistics.

Our work differs fundamentally from these approaches: instead of extracting local graph features, we compute the *effective resistance* of the entire graph—a global spectral property that captures overall connectivity and information flow capacity. This provides a single, interpretable scalar metric grounded in electrical network theory.

### 2.3 Deep Learning for Readability

Zhang et al. [5] propose a graph-based readability assessment method using Graph Convolutional Networks (GCNs) on part-of-speech dependency graphs. While their approach leverages graph structure, it requires training deep networks that learn features implicitly. In contrast, our effective resistance metric is *parameter-free* and directly interpretable: the Kirchhoff index has a clear physical meaning as the total resistance to information flow.

### 2.4 Information-Theoretic Approaches

Ehret [10] proposes using Kolmogorov complexity (via text compression) as a universal measure of language complexity. While both approaches use information theory concepts, effective resistance captures *discourse-level connectivity* while Kolmogorov complexity captures *lexical/syntactic redundancy*. The two approaches are complementary and could be combined in future work.

### 2.5 Cognitive Models of Readability

Klein et al. [7] demonstrate that surprisal (from language models) predicts reading ease measured via eye tracking. Our approach is complementary: effective resistance models *discourse structure* while surprisal models *lexical predictability*. Integrating both signals could yield a more complete cognitive model of readability.

## 3 Methods

### 3.1 Preliminaries: Effective Resistance and the Kirchhoff Index

The effective resistance between two nodes in a graph is derived from electrical network theory. Consider a graph $G = (V, E)$ with $|V| = n$ nodes. Assigning unit resistors to each edge, the *resistance distance* $R_{ij}$ between nodes $i$ and $j$ is the effective electrical resistance that would be measured between those nodes if the graph were an electrical circuit.

The *Kirchhoff index* (or effective graph resistance) is defined as the sum of resistance distances between all pairs of nodes:

$$\displaystyle Kf(G) = \sum_{i < j} R_{ij}$$

This can be computed efficiently from the graph Laplacian. Let $A$ be the adjacency matrix and $D = \text{diag}(\sum_j A_{ij})$ be the degree matrix. The graph Laplacian is $L = D - A$. The Moore-Penrose pseudoinverse $L^+$ of $L$ satisfies:

$$\displaystyle R_{ij} = L^+_{ii} + L^+_{jj} - 2L^+_{ij}$$

The Kirchhoff index is then:

$$\displaystyle Kf(G) = n \cdot \text{tr}(L^+) = \sum_{i=1}^n L^+_{ii}$$

where $n$ is the number of nodes [11].

Intuitively, graphs that are well-connected (many short paths between nodes) have low effective resistance, while sparse or poorly connected graphs have high effective resistance. We hypothesize that this property correlates with readability: coherent, well-structured text creates a "low-resistance" discourse graph, while disjointed text creates "high-resistance."

[ARTIFACT:art_IM3J27ltI7Pm]

Figure 2 illustrates the effective resistance readability scoring pipeline. Text is first sentence-tokenized, then converted to a discourse graph (currently using sequential edges), and finally the Kirchhoff index is computed from the Laplacian pseudoinverse.

[FIGURE:fig2]

### 3.2 Discourse Graph Construction

A critical design choice is how to construct the discourse graph from text. We investigate three approaches, progressively incorporating more sophisticated linguistic information.

#### 3.2.1 Sequential Graph (Baseline)

The simplest approach connects sentences in sequential order: node $i$ is connected to node $i+1$ for all $i$. Edge weights are uniform (1.0 in our implementation). This captures local coherence but misses long-distance semantic relationships.

#### 3.2.2 Similarity-Based Graph

We compute pairwise cosine similarity between sentence embeddings (using SBERT [12]) and add edges where similarity exceeds a threshold $\tau$. Edge weights are set to the similarity value. This captures semantic relatedness regardless of sentence position. The threshold $\tau$ controls graph density: higher $\tau$ yields sparser graphs.

#### 3.2.3 RST-Based Graph

Rhetorical Structure Theory (RST) parsers identify discourse relations between text spans (e.g., *elaboration*, *contrast*, *cause*). Edges are added based on these relations, with weights reflecting relation strength from parser confidence scores.

Due to computational constraints in our experimental environment, the current implementation uses the sequential graph only. Future work will incorporate similarity-based and RST-based constructions.

[ARTIFACT:art_IM3J27ltI7Pm]

### 3.3 Algorithm

Algorithm 1 summarizes the effective resistance readability scoring procedure.

```
Algorithm 1: Effective Resistance Readability Scoring
Input: Text T
Output: Readability score R(T)

1. Sentence-tokenize T → sentences s₁, ..., sₙ
2. if n < 2 then return 0  // Too short to assess
3. Construct adjacency matrix A ∈ {0,1}ⁿˣⁿ:
   for i = 1 to n-1 do
       A[i,i+1] = 1  // Sequential edges
       A[i+1,i] = 1
4. Compute degree matrix D = diag(∑ⱼ A[i,j])
5. Compute Laplacian L = D - A
6. Compute pseudoinverse L⁺ = pinv(L)
7. Compute Kirchhoff index:
   Kf = n × trace(L⁺)
8. Normalize: R(T) = -Kf/n  // Negate so higher = more difficult
9. return R(T)
```

The normalization in step 8 divides by $n$ to control for text length, and negates the result so that higher scores correspond to more difficult (less readable) text, matching the convention used by traditional readability formulas.

### 3.4 Computational Complexity

Computing the pseudoinverse of the Laplacian matrix costs $O(n^3)$ for dense matrices. For sparse graphs (e.g., sequential edges only), the Laplacian is also sparse, and iterative methods can compute the pseudoinverse more efficiently. In practice, for typical document lengths ($n < 100$ sentences), direct computation using `scipy.linalg.pinv` is sufficiently fast.

[ARTIFACT:art_rfw45zxdqTLX]

## 4 Experiments

### 4.1 Dataset

We evaluate our approach on a synthetically generated dataset of 50 texts spanning three readability levels: simple, medium, and complex. Each level contains 15-17 texts with varying sentence structures.

- **Simple texts** use common vocabulary, short sentences, and limited subordination (e.g., "The cat sat on the mat. It was happy there."). Human readability scores: 1-3.

- **Medium texts** use moderate vocabulary, longer sentences, and some subordination (e.g., "The restaurant prepared an elaborate meal for the distinguished guests who arrived promptly."). Human readability scores: 4-6.

- **Complex texts** use academic vocabulary, long sentences with multiple clauses, and domain-specific terminology (e.g., "The epistemological implications of quantum mechanics necessitate a paradigmatic reconceptualization."). Human readability scores: 7-10.

While synthetic data has limitations (discussed in Section 5), it provides ground-truth readability scores and allows controlled evaluation of whether the effective resistance metric can distinguish readability levels.

[ARTIFACT:art_rfw45zxdqTLX]

### 4.2 Baselines

We compare against five established readability metrics:

1. **Flesch-Kincaid Grade Level** [6]: Uses average sentence length and average word syllables.
2. **SMOG Index** [3]: Counts polysyllabic words (words with 3+ syllables).
3. **Coleman-Liau Index** [4]: Uses character-level features (letters per word, sentences per word).
4. **Average Sentence Length**: Simple baseline using only sentence length.
5. **Average Word Length**: Simple baseline using only word length.

All baselines are computed using the `textstat` library.

### 4.3 Evaluation Metrics

We report:

- **Pearson correlation coefficient** ($r$): Measures linear agreement between predicted and human scores.
- **Spearman rank correlation** ($\rho$): Measures monotonic agreement (more robust to outliers).
- **$p$-value**: Tests statistical significance of correlations.
- **Mean Absolute Error (MAE)** and **Root Mean Square Error (RMSE)**: Measure prediction accuracy.

### 4.4 Results

Table 1 presents the main results.

| Method | Pearson $r$ | Spearman $\rho$ | $p$-value | MAE | RMSE |
|--------|-------------|-----------------|-----------|-----|------|
| Effective Resistance | 0.80 | 0.81 | $< 10^{-12}$ | 0.52 | 0.64 |
| Flesch-Kincaid | 0.87 | 0.82 | $< 10^{-16}$ | 11.49 | 13.41 |
| SMOG | 0.85 | 0.86 | $< 10^{-15}$ | 8.25 | 9.72 |
| Coleman-Liau | 0.86 | 0.81 | $< 10^{-16}$ | 16.04 | 18.38 |
| Avg. Sentence Length | 0.82 | 0.79 | $< 10^{-13}$ | 5.93 | 6.68 |
| Avg. Word Length | 0.86 | 0.82 | $< 10^{-15}$ | 1.73 | 2.02 |

Table 1: Correlation results on synthetic dataset (N=50). All correlations are statistically significant at $p < 0.001$. The effective resistance metric achieves competitive performance despite using only sequential graph edges.

Key findings:

1. **Strong correlation**: The effective resistance metric achieves Pearson $r = 0.80$ and Spearman $\rho = 0.81$, both highly significant ($p < 10^{-12}$). This exceeds our target threshold of $r > 0.5$ for a "tiny experiment" and approaches the performance of traditional formulas.

2. **Competitive with baselines**: While Flesch-Kincaid ($r = 0.87$) and SMOG ($r = 0.85$) achieve slightly higher correlations, the effective resistance metric outperforms average sentence length ($r = 0.82$) and is competitive with Coleman-Liau ($r = 0.86$) in Spearman correlation.

3. **Differentiable metric**: Unlike traditional formulas that output on different scales, the effective resistance metric provides a continuous, differentiable score that could be used in optimization frameworks.

[ARTIFACT:art_rfw45zxdqTLX]

Figure 3 shows a scatter plot of effective resistance scores versus human readability judgments on the synthetic dataset. The strong linear trend (Pearson $r = 0.80$) confirms that the Kirchhoff index captures meaningful variance in readability.

[FIGURE:fig3]

Figure 4 compares the Pearson correlation coefficients across all evaluated readability metrics. The effective resistance metric (blue) achieves competitive performance with traditional formulas (orange), outperforming simple baselines like average sentence length.

[FIGURE:fig4]

### 4.5 Computational Performance

We measure runtime on the synthetic dataset (50 texts, 1-5 sentences per text). Results:

- **Average runtime per document**: 3.3 ms
- **Minimum runtime**: 0.013 ms (single-sentence text)
- **Maximum runtime**: 157.6 ms (longest text)
- **Total runtime for 50 documents**: 162.6 ms

These results demonstrate that the effective resistance metric is computationally feasible for real-time applications, meeting our target of < 1 s per document by a large margin.

Figure 5 shows the runtime analysis across documents of varying lengths. All runtimes are well under 1 second (maximum 157.6 ms), meeting real-time applicability requirements.

[FIGURE:fig5]

[ARTIFACT:art_rfw45zxdqTLX]

### 4.6 Ablation Study

Since the current implementation uses only sequential graphs, we cannot perform ablation over graph construction methods. However, we note that the sequential graph already captures local coherence, and the strong correlations achieved suggest that even this simple construction is informative for readability assessment. Future work will ablate over graph construction methods (sequential vs. similarity-based vs. RST-based) to quantify the contribution of each.

[ARTIFACT:art_rfw45zxdqTLX]

## 5 Discussion

### 5.1 Interpretation of Results

The strong correlation between effective resistance and human readability judgments provides initial support for our central hypothesis: readable text creates "low-resistance pathways" for information flow through coherent discourse connections. The Kirchhoff index captures this property as a global graph invariant, aggregating information from all pairwise resistance distances.

Interestingly, the effective resistance metric performs competitively despite using only sequential edges. This suggests that even local coherence (sequential sentence connectivity) carries significant information about readability. We hypothesize that incorporating semantic similarity edges would further improve performance by capturing long-distance coherence relations.

### 5.2 Limitations

Several limitations of the current study should be acknowledged:

1. **Synthetic dataset**: The use of synthetic texts with known readability levels enables controlled evaluation but may not fully capture the diversity of real-world text. The texts were designed to span readability levels but may not reflect naturalistic variation in discourse structure. Future work should evaluate on established benchmarks like the CLEAR corpus [13] or WeeBit [14].

2. **Sequential graph only**: The current implementation uses only sequential edges, missing semantic and discourse relations. This limits the method's ability to capture long-distance coherence. Implementing similarity-based and RST-based graph construction (Section 3.2) is a priority for future work.

3. **Small sample size**: With N=50 texts, the correlation estimates have relatively wide confidence intervals. A larger-scale evaluation is needed to confirm the results.

4. **Lack of eye-tracking validation**: The ultimate test of a readability metric is its ability to predict cognitive load during reading, measurable via eye tracking or other physiological signals. We do not have such data in the current study.

5. **Normalization sensitivity**: The normalization scheme (dividing by $n$ and negating) was chosen to make scores more interpretable, but the method's performance may be sensitive to this choice. Future work should investigate alternative normalization strategies.

[ARTIFACT:art_rfw45zxdqTLX]

### 5.3 Comparison to Prior Work

Our approach differs from prior graph-based coherence models [8, 9] in its use of a global spectral graph property (effective resistance) rather than local graph features. This provides a more holistic measure of discourse connectivity. However, the current results are preliminary, and a direct comparison on standard benchmarks is needed to establish superiority over these approaches.

Compared to deep learning approaches [5], our method has the advantage of interpretability: the Kirchhoff index has a clear physical interpretation. However, deep learning models can leverage large-scale pretraining and may achieve higher accuracy when sufficient labeled data is available. A hybrid approach combining effective resistance features with neural architectures is a promising direction.

### 5.4 Future Directions

Several avenues for future research emerge:

1. **Enhanced graph construction**: Implementing similarity-based edges using SBERT embeddings [12] and RST-based edges using discourse parsers would enrich the graph representation and likely improve correlation with human judgments.

2. **Evaluation on benchmarks**: Evaluating on standard readability corpora (CLEAR [13], WeeBit [14], OneStopEnglish [15]) would enable direct comparison with prior work and establish the method's generalizability.

3. **Cognitive validation**: Collecting eye-tracking data to validate whether effective resistance predicts reading times and comprehension would provide strong evidence for the cognitive plausibility of the metric.

4. **Hybrid models**: Combining effective resistance with traditional surface features and neural embeddings in a fusion model could leverage the strengths of each approach.

5. **Approximation algorithms**: For very long documents (>1000 sentences), exact computation of the pseudoinverse may be prohibitively expensive. Recent work on fast estimation of Laplacian pseudoinverse diagonal entries [16] could enable efficient approximation.

## 6 Conclusion

We have introduced a novel readability metric based on the effective electrical resistance of discourse graphs. By modeling text as an electrical circuit where sentences are connected by semantic pathways, the Kirchhoff index provides a physically-motivated, interpretable measure of readability that captures discourse-level coherence beyond surface features.

Evaluation on synthetic texts demonstrates that the effective resistance metric achieves strong correlation with human readability judgments (Pearson $r = 0.80$, Spearman $\rho = 0.81$), competitive with traditional formulas. The method is computationally efficient (3.3 ms per document) and provides a theoretically grounded alternative to black-box machine learning approaches.

While the current implementation uses only sequential graph edges, the framework is general and can incorporate richer discourse relations. Future work will enhance the graph construction, evaluate on standard benchmarks, and validate against cognitive measures of reading difficulty.

More broadly, this work demonstrates the value of cross-disciplinary transfer: concepts from electrical network theory can provide new insights into text analysis and readability assessment. We hope our physically-motivated approach inspires further research at the intersection of network science and natural language processing.

## Acknowledgments

[To be added]

## References

[1] Mesgar, M., & Strube, M. (2015). Graph-based Coherence Modeling For Assessing Readability. In *Proceedings of the Fourth Joint Conference on Lexical and Computational Semantics* (pp. 309-318).

[2] Flesch, R. (1948). A new readability yardstick. *Journal of Applied Psychology*, 32(3), 221-233.

[3] McLaughlin, G. H. (1969). SMOG grading: A new readability formula. *Journal of Reading*, 12(8), 639-646.

[4] Coleman, M., & Liau, T. L. (1975). A computer readability formula designed for machine scoring. *Journal of Applied Psychology*, 60(2), 283-284.

[5] Zhang, L., et al. (2026). Automatic text readability assessment for educational content based on graph representation learning. *Scientific Reports*, 16, 11308.

[6] Kincaid, J. P., et al. (1975). Derivation of new readability formulas (Automated Readability Index, Fog Count and Flesch Reading Ease Formula) for Navy enlisted personnel. Naval Technical Training Command.

[7] Klein, K. G., et al. (2025). Readability Formulas, Systems and LLMs are Poor Predictors of Reading Ease. In *Proceedings of the Conference on Empirical Methods in Natural Language Processing*. arXiv:2502.11150.

[8] Mesgar, M., & Strube, M. (2015). Graph-based Coherence Modeling For Assessing Readability. In *Proceedings of the Fourth Joint Conference on Lexical and Computational Semantics*.

[9] Guinaudeau, C., & Strube, M. (2013). Graph-based Local Coherence Modeling. In *Proceedings of the 51st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)* (pp. 93-103).

[10] Ehret, K. (2018). Kolmogorov complexity as a universal measure of language complexity. In *Proceedings of the Meeting of the Linguistic Association of Canada and the United States*.

[11] Ellens, W., et al. (2011). Effective graph resistance. *Linear Algebra and its Applications*, 435(10), 2491-2506.

[12] Reimers, N., & Gurevych, I. (2019). Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks. In *Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing*.

[13] CommonLit. (2023). CLEAR Corpus: CommonLit Ease of Readability. https://github.com/scrosseye/CLEAR-Corpus

[14] Deutsch, T., Jasbi, M., & Shieber, S. (2020). Linguistic Features for Readability Assessment. arXiv:2006.00377.

[15] Vajjala, S., & Lucic, I. (2018). OneStopEnglish corpus: A new corpus for automatic readability assessment and text simplification. In *Proceedings of the Workshop on Automatic Text Simplification* (pp. 297-304).

[16] Lu, Z., Xu, W., & Zhang, Z. (2023). Diagonal of Pseudoinverse of Graph Laplacian: Fast Estimation and Exact Results. arXiv:2310.05527.
</current_paper>

<reviewer_feedback>
Paper reviewer feedback from the previous iteration. Your strategy MUST address these critiques.
Prioritize major issues — these are the most impactful improvements to make.

- [MAJOR] (evidence) The effective resistance metric produces only TWO distinct values (-1.33 and 0.0) across all 50 test texts. This is because all texts in the synthetic dataset have either 1 sentence (34 texts) or 3 sentences (16 texts), and for a path graph, the Kirchhoff index depends only on the number of nodes. Specifically: (1) For 1-sentence texts, the code returns 0.0 (no edges); (2) For 3-sentence texts, the effective resistance is always 4/3, which after negation and normalization gives -1.33. The reported Pearson r=0.80 is entirely driven by the correlation between sentence count and human scores, not by any meaningful graph-theoretic property of the texts.
  Action: Replace the synthetic dataset with established readability corpora (CLEAR, WeeBit, OneStopEnglish) that contain texts with varying sentence counts and realistic discourse structure. Ensure the test set includes texts with 2-20+ sentences to properly evaluate whether effective resistance captures meaningful variance beyond sentence count. Alternatively, expand the synthetic dataset to include texts with diverse sentence counts (1-20+) and verify that the metric produces more than 2 distinct values.
- [MAJOR] (rigor) The MAE (0.52) and RMSE (0.64) reported for effective resistance are computed on z-normalized scores, not on the original human score scale (1-10). The actual raw MAE is 5.65 and RMSE is 6.12, which are enormous errors for a 1-10 scale. The normalization makes the errors appear misleadingly small and incomparable to the baseline metrics, which are reported on their original scales (Flesch-Kincaid grade levels). This is a significant methodological error that undermines the paper's claims about prediction accuracy.
  Action: Recompute MAE/RMSE on the original scale (1-10) and report those values. Either: (1) Learn a linear transformation from ER scores to human scores via regression and report errors on that scale, or (2) Report correlation metrics (Pearson/Spearman) as the primary evaluation and move MAE/RMSE to a secondary role with clear scale information. Ensure all metrics in Table 1 are comparable.
- [MAJOR] (methodology) The paper claims to model 'discourse graphs' where 'sentences are nodes and discourse connections are resistors.' However, the implementation (Section 3.2.1, Algorithm 1) only constructs sequential edges (sentence i connected to i+1). This is simply a path graph—there are no actual discourse connections, semantic similarity edges, or RST-based relations. The paper acknowledges this limitation in Section 4.6, but the main results and abstract present the method as if it captures discourse coherence. Without semantic or discourse edges, the 'effective resistance' is essentially a complex way to count sentences.
  Action: Either: (1) Implement the similarity-based graph construction (Section 3.2.2) using SBERT embeddings to add semantic edges, which would make the 'discourse graph' claim valid, or (2) Reframe the paper as proposing 'sequential graph resistance' rather than 'discourse graph resistance' and adjust claims accordingly. The current gap between claims and implementation is too large.
- [MAJOR] (evidence) The evaluation uses a synthetic dataset of 50 texts with human readability scores assigned by formula (simple=1-3, medium=4-6, complex=7-10) rather than actual human judgments. The texts are artificially constructed and do not reflect naturalistic variation in discourse structure. Section 5.2 acknowledges this limitation, but the entire experimental validation rests on this dataset. Without evaluation on real texts with genuine human readability assessments, the results are not generalizable.
  Action: Evaluate on at least one established readability corpus with real human judgments. The CLEAR corpus (CommonLit Ease of Readability) and WeeBit dataset are both referenced in the paper (References 13, 14) and readily available. Even a small-scale evaluation on 100-200 texts from these corpora would provide much stronger evidence than the synthetic dataset.
- [MINOR] (methodology) The normalization scheme in Algorithm 1 (step 8: R(T) = -Kf/n) negates the Kirchhoff index and divides by n. However, the motivation for this normalization is not well-justified. The Kirchhoff index naturally increases with the number of nodes, so dividing by n makes some sense, but the negation is arbitrary (simply inverting the interpretation). More importantly, this normalization does not account for graph density—a key factor in effective resistance.
  Action: Provide theoretical justification for the normalization scheme. Consider alternative normalization strategies such as: (1) Dividing by n^2 to account for the quadratic growth of pairwise resistances, or (2) Using the average resistance distance (Kf / nC2) instead of Kf/n. Compare normalization strategies in the evaluation.
- [MINOR] (clarity) The runtime analysis reports 3.3 ms per document, but the test documents have only 1-3 sentences. This gives a misleading impression of computational efficiency. For a document with 100 sentences, the O(n^3) pseudoinverse computation would take ~3.3 * (100/3)^3 ≈ 122,000 ms = 122 seconds, which is not real-time feasible.
  Action: Report runtime scaling analysis: measure runtime for documents with 10, 50, 100, and 500 sentences and plot the n^3 scaling. Provide more realistic runtime estimates for typical document lengths. If the method is too slow for long documents, discuss approximation strategies (referenced in Section 5.4, point 5).
- [MINOR] (novelty) While using effective resistance (Kirchhoff index) for readability is novel, the connection between graph resistance and text coherence is not entirely new. Prior work on graph-based coherence modeling (Mesgar & Strube 2015, Guinaudeau & Strube 2013) uses graph properties like outdegree and connectivity. The novelty is in using a global spectral property rather than local features. However, the paper could do more to explain why effective resistance is superior to simpler graph invariants (e.g., average path length, graph diameter).
  Action: Add a theoretical analysis comparing effective resistance to other graph invariants. Show empirically (on a small example) how effective resistance differs from simpler metrics like average node degree or graph diameter. This would strengthen the case for why effective resistance is the right metric to use.
</reviewer_feedback>

<task>
Generate 1 research strategy for THIS iteration.

**ARTIFACT LIMIT: Each strategy may contain AT MOST 3 artifact directions.** Focus on the highest-impact artifacts. Quality over quantity.

Each strategy should:
1. Define a clear OBJECTIVE - what novel contribution we're building toward
2. Plan artifacts to execute NOW - specify type, objective, approach, and depends_on for each
3. Account for parallel execution - all strategies and all planned artifacts run simultaneously, their artifacts are combined into one shared pool


</task><user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_RiHQW43yNEvO/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_RiHQW43yNEvO/3_invention_loop/iter_2/gen_strat/gen_strat_1/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "ArtifactDep": {
      "description": "A single dependency on an existing artifact, with a short type label.\n\n``id`` and ``label`` are LLM-generated at strategy time. ``label`` is free-text but\nshort \u2014 a word or two naming the type of dependency, not a sentence.\n\n``relation_type`` and ``relation_rationale`` are populated later, in upd_hypo,\nusing the MultiCite citation-function typology (Lauscher et al., NAACL 2022).\nThey are absent at strategy time and may stay absent for legacy runs.",
      "properties": {
        "id": {
          "description": "ID of an existing artifact this artifact depends on",
          "title": "Id",
          "type": "string"
        },
        "label": {
          "description": "Short free-text label naming the type of this dependency (a word or two, not a sentence)",
          "title": "Label",
          "type": "string"
        }
      },
      "required": [
        "id",
        "label"
      ],
      "title": "ArtifactDep",
      "type": "object"
    },
    "ArtifactDirection": {
      "description": "High-level direction for an artifact to execute this iteration.\n\nID is code-assigned (LLMPrompt only \u2014 visible in prompts, not LLM-generated).",
      "properties": {
        "type": {
          "description": "Type of artifact to create",
          "enum": [
            "experiment",
            "research",
            "proof",
            "evaluation",
            "dataset"
          ],
          "title": "Type",
          "type": "string"
        },
        "objective": {
          "description": "What we want to achieve with this artifact",
          "title": "Objective",
          "type": "string"
        },
        "approach": {
          "description": "High-level direction/method",
          "title": "Approach",
          "type": "string"
        },
        "depends_on": {
          "description": "Existing artifacts this depends on, each with a short type label",
          "items": {
            "$ref": "#/$defs/ArtifactDep"
          },
          "title": "Depends On",
          "type": "array"
        }
      },
      "required": [
        "type",
        "objective",
        "approach"
      ],
      "title": "ArtifactDirection",
      "type": "object"
    },
    "Strategy": {
      "description": "A research strategy.\n\nContent fields have LLMPrompt + LLMStructOut markers.\n``id`` is code-assigned (LLMPrompt only \u2014 visible in prompts, not LLM-generated).\n\nID format: gen_strat_idx{N}",
      "properties": {
        "title": {
          "description": "Strategy name in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance and it fits the run visualizations. Aim for about 4-8 words (~40 characters).",
          "title": "Title",
          "type": "string"
        },
        "objective": {
          "description": "The novel contribution we're building toward",
          "title": "Objective",
          "type": "string"
        },
        "rationale": {
          "description": "Why this strategy is promising",
          "title": "Rationale",
          "type": "string"
        },
        "artifact_directions": {
          "description": "Artifacts to execute THIS iteration",
          "items": {
            "$ref": "#/$defs/ArtifactDirection"
          },
          "title": "Artifact Directions",
          "type": "array"
        },
        "expected_outcome": {
          "description": "What we'll have after this iteration's artifacts complete",
          "title": "Expected Outcome",
          "type": "string"
        },
        "summary": {
          "default": "",
          "description": "Brief summary of the strategy and its expected contribution",
          "title": "Summary",
          "type": "string"
        }
      },
      "required": [
        "title",
        "objective",
        "rationale",
        "artifact_directions",
        "expected_outcome"
      ],
      "title": "Strategy",
      "type": "object"
    }
  },
  "description": "Top-level wrapper for LLM strategy generation output.",
  "properties": {
    "strategies": {
      "description": "List of generated strategies",
      "items": {
        "$ref": "#/$defs/Strategy"
      },
      "title": "Strategies",
      "type": "array"
    }
  },
  "required": [
    "strategies"
  ],
  "title": "Strategies",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `/ai-inventor/aii_data/runs/run_RiHQW43yNEvO/3_invention_loop/iter_2/gen_strat/gen_strat_1/.sdk_openhands_agent_struct_out.json`.
````

### [2] HUMAN-USER prompt · 2026-07-08 11:17:06 UTC

```
Propose a simple, novel, testable ML method for scoring text readability and validate it with a tiny experiment.
```

### [3] SYSTEM-USER prompt · 2026-07-08 11:20:34 UTC

```
<verification_results>
Your previous response had issues that need fixing:

DEPENDENCY ERRORS (depends_on can ONLY reference IDs from <existing_artifacts>):
  - Strategy 1: Artifact 'experiment_iter2_dir2' (experiment): missing required dependency. Must have at least one dependency of type: {'dataset'}

</verification_results>

<task>
Fix ALL issues above and regenerate your strategies:

1. Fix dependency errors:
   - depends_on is a list of {id, label} objects — every entry MUST have a non-empty short label
   - id can ONLY reference IDs from <existing_artifacts>
   - You CANNOT reference artifacts you are proposing in this strategy as dependencies (they all run in parallel)
   - Follow the dependency type rules (e.g., experiments require datasets)
   - If no suitable existing artifacts exist, use depends_on: []

Output the corrected JSON with the fixed strategies.
</task>
```
