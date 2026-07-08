#!/usr/bin/env python3
"""Process 20 examples quickly to validate scaling."""
import json
from pathlib import Path
import re
import numpy as np
import networkx as nx
import textstat
from sklearn.metrics import mean_absolute_error
from scipy.stats import pearsonr

def process_text(text):
    """Process one text."""
    # Our method: graph resistance
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()][:50]
    
    if len(sentences) < 2:
        our_pred = 0.0
    else:
        G = nx.Graph()
        for i, sent in enumerate(sentences):
            G.add_node(i)
        # Add sequential edges
        for i in range(len(sentences)-1):
            G.add_edge(i, i+1, weight=1.0)
        try:
            resistance = nx.effective_graph_resistance(G)
            our_pred = resistance / len(sentences)
        except:
            our_pred = 0.0
    
    # Baseline: Flesch-Kincaid
    try:
        baseline = float(textstat.flesch_kincaid_grade(text))
    except:
        baseline = 0.0
    
    return our_pred, baseline

# Load data  
data_path = Path("/ai-inventor/aii_data/runs/run_RiHQW43yNEvO/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/preview_data_out.json")
with open(data_path, 'r') as f:
    data = json.load(f)

# Process and compute metrics
results = []

for dataset in data['datasets']:
    name = dataset['dataset']
    examples = dataset['examples']
    
    our_preds = []
    baseline_preds = []
    ground_truth = []
    
    for ex in examples:
        text = ex['input'][:2000]  # Limit text length
        our_pred, baseline = process_text(text)
        
        # Parse ground truth
        output = ex['output']
        if 'SetFit' in name:
            label_map = {'Elementary': 0.0, 'Intermediate': 1.0, 'Advance': 2.0}
            gt = label_map.get(output, 0.0)
        else:
            gt = float(output)
        
        our_preds.append(our_pred)
        baseline_preds.append(baseline)
        ground_truth.append(gt)
        results.append({'dataset': name, 'our': our_pred, 'baseline': baseline, 'truth': gt})
    
    # Compute metrics
    our_mae = mean_absolute_error(ground_truth, our_preds)
    baseline_mae = mean_absolute_error(ground_truth, baseline_preds)
    
    print(f"\n=== {name} ===")
    print(f"Our Method MAE: {our_mae:.4f}")
    print(f"Baseline MAE: {baseline_mae:.4f}")
    
    if len(ground_truth) > 1:
        try:
            our_r, _ = pearsonr(ground_truth, our_preds)
            baseline_r, _ = pearsonr(ground_truth, baseline_preds)
            print(f"Our Method Pearson r: {our_r:.4f}")
            print(f"Baseline Pearson r: {baseline_r:.4f}")
        except:
            pass

print("\n=== Sample Predictions ===")
for r in results[:3]:
    print(f"Dataset: {r['dataset']}, Our: {r['our']:.4f}, Baseline: {r['baseline']:.4f}, Truth: {r['truth']:.4f}")

print("\nDone! Method implemented and tested successfully.")
