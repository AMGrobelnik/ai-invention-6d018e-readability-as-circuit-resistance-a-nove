# gen_paper_text — test_idea

> Phase: `invention_loop` · round 1 · `gen_paper_text`
> Run: `run_RiHQW43yNEvO` — Simple Readability Score
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_paper_text` (sdk_openhands_agent)

### [1] SYSTEM-USER prompt · 2026-07-08 10:58:49 UTC

````
<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. Use it for related-work positioning and how this field frames a genuinely novel contribution.

- **aii-handbook-multi-llm-agents** — Guide for implementing Multi-LLM Agent Systems research using Mirascope orchestration, HuggingFace datasets/evaluation, and proven multi-agent patterns.
</available_domain_handbooks>
<hypothesis>
The research hypothesis.

kind: hypothesis
title: Readability as Circuit Resistance
hypothesis: >-
  Text readability can be accurately modeled through the effective electrical resistance of a discourse graph. When sentences
  are represented as nodes and semantic discourse connections as weighted edges (resistors), the total effective resistance
  (Kirchhoff index) of this graph provides a novel, physically-motivated readability metric. The key insight is that readable
  text creates 'low-resistance pathways' for information flow - coherent discourse with strong semantic connections allows
  information to flow easily (low resistance), while disjointed or complex text impedes information flow (high resistance).
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
</hypothesis>

<all_artifacts>
FULL EVIDENCE BASE: All 3 research artifacts across all iterations.

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
</all_artifacts>

<new_artifacts_this_iteration>
NEW THIS ITERATION: These 3 artifacts were created to address the reviewer
feedback. Their findings should be the primary basis for your revisions.

id: art_IM3J27ltI7Pm
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
type: research
title: Effective Resistance for Readability Graphs Research

id: art_vYMmBxe-2BfW
summary: >-
  Successfully collected 4 readability datasets from HuggingFace Hub, evaluated their provenance via web research, and selected
  the 2 best datasets for the experiment. The selected datasets are: 1) SetFit/onestop_english (567 examples, 3-class classification:
  Elementary/Intermediate/Advance) - an established benchmark with published paper (Vajala and Lučić, 2018), and 2) agentlans/readability
  (104,761 examples, regression with continuous grade scores 0-20) - diverse text sources including Wikipedia, ArXiv, and
  Fineweb-Edu. Both datasets were standardized to exp_sel_data_out.json schema with input (text), output (readability label/score),
  and metadata fields (fold, task_type, etc.). The full dataset (119MB) was split into 2 parts under 100MB each as required.
  All outputs validated against schema and preview/mini versions generated.
type: dataset
title: Readability datasets for ML scoring

id: art_rfw45zxdqTLX
summary: >-
  Implemented and evaluated a novel effective resistance metric for text readability using discourse graphs. The method constructs
  a graph where sentences are nodes and edges represent discourse connections (sequential in this implementation). The Kirchhoff
  index (sum of effective resistances between all node pairs) serves as the readability score. Evaluated on 50 synthetic texts
  with known readability levels (simple/medium/complex). Results show strong correlation with human readability scores (Pearson
  r=0.80, Spearman ρ=0.81, p<0.001) and competitive performance with baseline metrics (Flesch-Kincaid r=0.87, SMOG r=0.85).
  The method is computationally efficient (0.004s per document) and provides a theoretically grounded alternative to traditional
  readability formulas. Limitations: current implementation uses sequential graphs only (no semantic similarity edges) due
  to environment constraints; future work should incorporate sentence embeddings for enhanced performance.
type: experiment
title: Circuit Resistance Readability Test
</new_artifacts_this_iteration>

<data_files>
Data files come in three sizes:
- preview_*_out.json — READ THIS to inspect the data structure
- mini_*_out.json (~3 examples) — use for prototyping/testing
- full_*_out.json (complete) — use for the final production run. NEVER open it directly (too large to read into context). Instead, extract values programmatically with shell commands (e.g. grep) or a Python script (use aii-long-running-tasks skill for scripts).
</data_files>

<task>
Write a research paper draft with LaTeX-ready text, BibTeX citations, and figure placeholders.

This is the FIRST paper draft. Write a complete research paper from scratch based on the hypothesis and all available artifacts.
</task>

<figure_instructions>
FIGURE FORMAT: Use [FIGURE:fig_id] markers in paper_text to indicate where each figure goes.
Then provide the full figure specs in the separate `figures` structured output array.
Each figure in the array must have an `id` matching a marker in the text. Set the `aspect_ratio`
field per figure: 21:9 for architecture / pipeline / flow-chart diagrams (the hero figure should
be one of these — place its marker near the END of the Introduction so it floats to the top of
page 2), 16:9 for comparisons / multi-panel results, 4:3 for dense charts, 1:1 for heatmaps /
confusion matrices / scatter plots.

Example in paper_text:
  "...our method achieves state-of-the-art results as shown below.\n\n[FIGURE:fig3]\n\nThe results demonstrate..."

Example in figures array (results comparison):
  {"id": "fig3", "title": "Performance Comparison", "caption": "Comparison of geometric mean query latency across optimizers.", "image_gen_detailed_description": "Grouped bar chart. X-axis: model names. Y-axis: latency (seconds, 0-5). Values: PostgreSQL=4.6s (red), Bao=2.8s (blue), RLQOpt=2.0s (green). Error bars +/-0.3-0.8. Sans-serif font, white background.", "aspect_ratio": "16:9", "summary": "Compares latency across optimizers"}

Example in figures array (architecture diagram, hero):
  {"id": "fig1", "title": "System Architecture", "caption": "End-to-end pipeline: encoder feeds latents into the planner, which queries the value head before emitting actions.", "image_gen_detailed_description": "Horizontal flow diagram, left to right. Five labeled boxes: 'Input' (gray), 'Encoder' (blue), 'Latent (z, 256-dim)' (light blue, narrow), 'Planner' (green), 'Action Head' (orange). Arrows labeled with shapes. Value head as separate green box below 'Planner', bidirectional arrow. Sans-serif font, clean white background, no 3D.", "aspect_ratio": "21:9", "summary": "Hero architecture diagram"}

CRITICAL: Before writing figure specs, look through artifact workspace output files (*_out.json)
and code to find ALL the exact values. The figure generator cannot read files — every exact number
and value MUST be in the image_gen_detailed_description.
</figure_instructions>

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-paper-writing, aii-semscholar-bib.
TODO 2. LITERATURE REVIEW: Use web search tools to research the landscape — search key terms from
<hypothesis> and <all_artifacts>. Then use aii_semscholar_bib__fetch to batch-fetch real
BibTeX entries. Build a comprehensive Related Work section. Do NOT fabricate entries.
TODO 3. READ ARTIFACTS: Before writing each section, READ the relevant artifact source code, output
files, and data in the workspace. Extract concrete implementation details, technical innovations,
algorithmic specifics, and quantitative results. Do NOT write surface-level descriptions.

ARTIFACT REFERENCES: When you reference results, methodology, or findings from a specific artifact,
place an [ARTIFACT:artifact_id] marker inline. These become footnotes linking to the artifact's code
in the GitHub repository (first mention gets a footnote with URL, subsequent mentions are omitted).
Use the exact artifact ID from <all_artifacts>. Place the marker right after the claim it supports.
Example:
  "Our evaluation showed a 15% improvement over baselines [ARTIFACT:art_4f9d2c81ab37]." 
TODO 4. WRITE PAPER: Write the full paper text with [FIGURE:fig_id] markers per <figure_instructions>,
and provide the figure specs in the figures array. Cite with numeric references [1], [2], etc.
At the end of the paper text, include a full bibliography section. Do NOT compile LaTeX or generate
actual image/figure files. Your ONLY output is the structured JSON.
</todos><user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_RiHQW43yNEvO/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_RiHQW43yNEvO/3_invention_loop/iter_1/gen_paper_text/gen_paper_text/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "FigureSpec": {
      "description": "Figure specification \u2014 structured output from paper writing agent.\n\nThe LLM fills these as a list in PaperText.figures.\nLater converted to Figure objects for viz gen.",
      "properties": {
        "id": {
          "description": "Figure ID matching the [FIGURE:id] marker in paper_text (e.g., 'fig1')",
          "title": "Id",
          "type": "string"
        },
        "title": {
          "description": "Figure title in plain, everyday language \u2014 short and jargon-free. Aim for about 4-8 words (~40 characters).",
          "title": "Title",
          "type": "string"
        },
        "caption": {
          "description": "LaTeX figure caption \u2014 appears below the figure in the paper. Should describe what the figure shows and highlight key takeaways.",
          "title": "Caption",
          "type": "string"
        },
        "image_gen_detailed_description": {
          "description": "Detailed image generation prompt \u2014 axes, labels, ALL numeric values, colors, aspect ratio, layout. The image generator cannot read files; this is its ONLY input.",
          "title": "Image Gen Detailed Description",
          "type": "string"
        },
        "summary": {
          "description": "Brief summary of what this figure communicates",
          "title": "Summary",
          "type": "string"
        }
      },
      "required": [
        "id",
        "title",
        "caption",
        "image_gen_detailed_description",
        "summary"
      ],
      "title": "FigureSpec",
      "type": "object"
    }
  },
  "description": "Paper text \u2014 structured output from paper writing agent.\n\nStructured output fields (LLMPrompt + LLMStructOut):\n- title, abstract, paper_text, figures, summary\n\npaper_text contains [FIGURE:fig_id] markers for positioning.\nfigures contains the full specs as structured objects.\n\nMetadata fields (plain, set by pipeline code):\n- id",
  "properties": {
    "title": {
      "description": "Paper title \u2014 clear, plain-language, and short so a non-expert understands the main contribution at a glance. Aim for about 6-10 words; avoid jargon and acronyms.",
      "title": "Title",
      "type": "string"
    },
    "abstract": {
      "description": "Paper abstract",
      "title": "Abstract",
      "type": "string"
    },
    "paper_text": {
      "description": "Full paper body text with markdown section headers (# Introduction, # Methods, # Results, # Discussion, # Conclusion). Use [FIGURE:fig_id] markers (e.g. [FIGURE:fig1]) to indicate where each figure should appear.",
      "title": "Paper Text",
      "type": "string"
    },
    "figures": {
      "description": "List of figure specifications. Each must have an id matching a [FIGURE:id] marker in paper_text.",
      "items": {
        "$ref": "#/$defs/FigureSpec"
      },
      "title": "Figures",
      "type": "array"
    },
    "summary": {
      "description": "Brief summary of the paper's main contribution and findings",
      "title": "Summary",
      "type": "string"
    }
  },
  "required": [
    "title",
    "abstract",
    "paper_text",
    "summary"
  ],
  "title": "PaperText",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `/ai-inventor/aii_data/runs/run_RiHQW43yNEvO/3_invention_loop/iter_1/gen_paper_text/gen_paper_text/.sdk_openhands_agent_struct_out.json`.
````

### [2] HUMAN-USER prompt · 2026-07-08 10:58:49 UTC

```
Propose a simple, novel, testable ML method for scoring text readability and validate it with a tiny experiment.
```

### [3] SKILL-INPUT — aii-paper-writing · 2026-07-08 10:59:03 UTC

The agent loaded the **aii-paper-writing** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-paper-writing
description: Academic paper writing guidance for AI research. Covers paper structure, figure placeholders, bibliography building with Semantic Scholar, and citation rules. Does NOT cover LaTeX compilation or figure file generation — see aii-paper-to-latex for that.
---

## Technical Papers

Guidance for the standard "technical paper" format: propose a method/system/framework, evaluate it experimentally, report results. This is the main track at most CS venues (NeurIPS, ICML, ICLR, ACL, AAAI, etc.). Does NOT cover: pure theory/formal proofs, survey papers, position papers, or dataset/benchmark papers — those have different structures.

### Paper Structure

Target 6-8 pages. Use formal academic language, third person. Support claims with evidence from artifacts.

#### Rough Page Budget (8-page paper)

| Section | Pages | Notes |
|---|---|---|
| Abstract | 0.3 | Problem, approach, key result |
| Introduction | 1.0-1.5 | The most important section |
| Related Work | 0.5-1.0 | Beginning or end (see below) |
| Methods | 1.5-2.0 | Architecture fig on page 1 |
| Experiments | 1.5-2.0 | Setup + results + ablations |
| Discussion | 0.5-1.0 | Limitations go here |
| Conclusion | 0.3-0.5 | Do not repeat the abstract |
| References | 0.5-1.0 | Not counted in page limit |

**Critical rule**: A clear new technical contribution must be articulated by page 3 (quarter of the paper). If the reader doesn't know what you did by then, you've lost them.

#### Section Details

**Abstract** (150-250 words): State the problem, your approach, and the main results. Be factual and comprehensive. Do not repeat the abstract word-for-word later in the paper.

**Introduction** — Follow this 5-paragraph structure:

1. **What is the problem?** Define the task concretely.
2. **Why is it interesting and important?** Real-world impact, scale.
3. **Why is it hard?** Why do naive approaches fail?
4. **Why hasn't it been solved before?** What's wrong with prior solutions? How does yours differ?
5. **What are the key components of your approach and results?** Include specific limitations.

End with a "Summary of Contributions" subsection — bullet list of contributions with section references. This doubles as an outline, saving space.

**Related Work** — Placement decision:
- **Beginning** (Section 2): If it can be short yet detailed, or if you need a strong defensive stance against prior work early.
- **End** (before Conclusions): If comparisons require your technical content, or if it can be summarized briefly in the Introduction. Can be titled "Discussion and Related Work."

**Methods/Approach**: Every section tells a story — the story of the results, NOT the story of how you arrived at them. Use top-down description: readers should see where the material is going and be able to skip ahead. Move gory details to appendices.

**Experiments**: Setup (datasets, metrics, baselines) → main results → ablations → analysis. Every claim needs quantitative evidence.

**Discussion**: Interpret results, compare to prior work, state limitations honestly. Limitations should be specific and actionable, not vague disclaimers.

**Conclusion**: Short summarizing paragraph. Do NOT repeat material from the Abstract or Introduction. Make original claims more concrete (e.g., reference quantitative results). Include future work as bullet list — if actively pursuing follow-up, say so to mark territory.

#### Writing Quality Rules

- Define all notation/terminology before use, only once. Group global definitions in Preliminaries.
- Do NOT use nonreferential "this", "that", "these", "it". Always specify the referent. BAD: "This is important because..." GOOD: "This accuracy gap is important because..."
- Do NOT use "etc." unless remaining items are completely obvious. BAD: "We measure volatility, scalability, etc." GOOD: "We measure volatility and scalability."
- Do NOT write "for various reasons" — state the actual reasons.
- "That" is defining, "which" is nondefining. "The algorithms that are easy to implement" vs "The algorithms, which are easy to implement."
- Use italics for definitions and quotes, not for emphasis. Context alone should provide emphasis.

### Figure Format

Figures use a hybrid marker + structured array approach. ALL figures are generated by a separate pipeline step using an AI image model — your `image_gen_detailed_description` is the ONLY input that model sees. It cannot read files or access data. Do NOT generate actual image files yourself (no matplotlib, no PIL, no image generation scripts).

**In paper_text**: Place `[FIGURE:fig_id]` markers where figures should appear.

**In figures array**: Provide full specs as structured objects with these fields:
- `id` — matches the `[FIGURE:id]` marker in paper_text
- `title` — short descriptive title
- `caption` — LaTeX caption that appears below the figure in the paper
- `image_gen_detailed_description` — detailed prompt for the image generator (axes, ALL values, colors, layout)
- `summary` — brief summary of what the figure communicates

Example in paper_text:
```
...our method achieves state-of-the-art results as shown below.

[FIGURE:fig_1]

The results in Figure 1 demonstrate...
```

Example figure spec in figures array:
```json
{"id": "fig_1", "title": "Performance Comparison", "caption": "Comparison of geometric mean query latency across optimizers on JOB benchmark. RLQOpt achieves 2.3x speedup over PostgreSQL.", "image_gen_detailed_description": "Grouped bar chart. X-axis: model names. Y-axis: accuracy (0.0-1.0). Values: ModelA=0.847, ModelB=0.762, Baseline=0.531. Error bars with std: 0.02, 0.03, 0.05. Sans-serif font, white background.", "summary": "Compares accuracy of proposed methods vs baseline."}
```

Every marker in text MUST have a matching figure in the array, and vice versa.

#### Data Precision Requirement

`image_gen_detailed_description` MUST include exact numbers from artifact output files. Read the actual output files before writing figure specs.

- BAD: "Compare accuracy metrics across configurations"
- GOOD: "Grouped bar chart. X-axis: model names. Y-axis: accuracy (0.0-1.0). Values: K=3: 0.765, K=5: 0.729, Baseline: 0.121."

#### Figure vs Table Decision

Do NOT create figures for tabular data (rows/columns of text or numbers). Use `\begin{table}` in LaTeX instead. Figures are for actual visualizations only (charts, plots, diagrams).

#### Figure Placement Strategy

Be intentional with figure ordering. The architectural/method overview figure explaining the proposed approach MUST appear early — in the Introduction or at the start of Methods — so readers can immediately orient themselves. Readers skim papers top-down; if the first figure they see is a results bar chart, they have no mental model for interpreting it.

Recommended ordering:
1. **Architecture/method diagram** — Introduction or early Methods (so readers understand the approach before diving into details)
2. **Conceptual/analogy figures** — Introduction or Methods (to build intuition)
3. **Results figures** (bar charts, line plots, scatter plots) — Results section
4. **Analysis/ablation figures** — Discussion or later Results

#### Guidelines

- Plan 3-6 figures total across the paper
- Place [FIGURE:fig_id] markers INLINE where referenced in text
- Include axes, labels, ALL numeric values in figure descriptions
- Both data-driven figures (bar charts, line plots) and conceptual diagrams (architecture, flowcharts)
- Be as detailed as possible in descriptions: specify aspect ratio, preferred colors, all data values, axis labels, ranges, legend entries, and any other visual details. The more specific the description, the better the generated figure

### Bibliography with Semantic Scholar

Build `./references.bib` using the aii-semscholar-bib skill (real BibTeX from Semantic Scholar):

1. Collect DOIs, ArXiv IDs, or titles for all papers you need to cite
2. Call `aii_semscholar_bib__fetch` with the full list in one batch
3. Write the returned .bib text into `./references.bib`

Rules:
- Do NOT fabricate BibTeX entries — always fetch from Semantic Scholar
- If a paper isn't found (very recent preprint), write the entry manually as fallback
- Use `\bibliography{references}` and `\bibliographystyle{plainnat}`
- Do NOT use inline `thebibliography` environment

### Citation Format (for Research Artifacts)

When writing research with numbered citations:

1. Every factual claim MUST have a numbered citation: `[1]`, `[2]`, `[1, 3]`, etc.
2. Each source in the "sources" array MUST have an "index" field
3. The index MUST EXACTLY MATCH citation numbers in the text
4. NEVER cite a number without a matching source index
5. Example: "LLMs show 40% improvement with multi-agent collaboration [1]."
````

### [4] SKILL-INPUT — aii-semscholar-bib · 2026-07-08 10:59:03 UTC

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

### [5] SKILL-INPUT — aii-web-tools · 2026-07-08 11:00:00 UTC

The agent loaded the **aii-web-tools** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-web-tools
description: "Web research toolkit: web search (Serper/Google), web page fetch as markdown (HTML and PDF), and regex grep over full page/PDF text. Use whenever a task needs to search the web, read a page, mine a paper/PDF, verify citations, or extract exact quotes, numbers, or methodology from a URL."
---

## Web tools

You have three web capabilities: **search**, **fetch**, and **grep** (exact
regex extraction over a full page or PDF).

**Pick where they come from, in this order:**

1. **If you have built-in `WebSearch` / `WebFetch` tools, PREFER those over the
   scripts below.** They may be **deferred tools** (listed by name but with
   schemas not yet loaded) — if so, call `ToolSearch("select:WebSearch,WebFetch")`
   ONCE to load them, then use them normally. Do not skip them just because they
   need that one extra load step; they are the preferred path. Pair them with the
   `aii_web_tools__fetch_grep` script below when you need exact text / numbers /
   methodology that a summary would miss, or when reading a PDF.
2. **Only if you have NO built-in `WebSearch` / `WebFetch`** (e.g. the OpenHands
   backend), use the scripts in this skill (below). They are our own
   implementations — Serper.dev for search, html2text + PyMuPDF for fetch, and
   regex grep over the full document text. They work without any built-in web
   tools.

Workflow either way: **search** (discover) → **fetch** (read for the gist) →
**grep** (pull exact details / read PDFs).

---

## Running the scripts

Run every script with the skill's pre-provisioned interpreter (it already has
`requests`, `html2text`, `pymupdf`, `python-dotenv`). Set `PY` once:

```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
```

### 1. Search the web (Serper.dev / Google)

```bash
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "neuro-symbolic FOL translation LLM" --max-results 10
```

Returns ranked title / URL / snippet lines. Use it first to scan the
landscape; snippets are for discovery only — fetch a page before judging it.

### 2. Fetch a page as markdown (HTML or PDF)

```bash
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" fetch --url "https://arxiv.org/abs/2303.11366" --max-chars 10000
```

`--max-chars` caps output (default 10000); `--char-offset N` pages further in.
Handles PDFs transparently via PyMuPDF.

### 3. Grep a page or PDF (exact regex extraction)

```bash
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" grep --url "https://arxiv.org/pdf/2303.11366" --pattern "verbal reinforcement" --max-matches 20 --context-chars 200
```

Returns only the matching sections with surrounding context — the right tool
for exact numbers, table values, methodology, or long PDFs where a summary
would lose the detail. `-i` for case-insensitive.

**Parallelize** independent searches/fetches in one turn; only sequence a
fetch after the search that produced its URL.

---

## Notes

- The scripts call our ability server. If a script prints
  `Ability service not available`, the server is down — say so rather than
  silently improvising a different search method.
- Do **not** hand-roll your own `requests`/scraping for search when these
  tools are available: Serper returns clean Google results and the fetch/grep
  scripts already handle HTML, PDFs, and encoding.
````
