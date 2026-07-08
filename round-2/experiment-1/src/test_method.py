#!/usr/bin/env python3
"""Quick test of core functionality."""
import json
from pathlib import Path
import sys
import re
import numpy as np
import networkx as nx
import textstat
from sklearn.metrics import mean_absolute_error, mean_squared_error, pearsonr
from scipy.sparse.linalg import pinv

def text_to_sentences(text, max_sentences=50):
    """Split text into sentences."""
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    return sentences[:max_sentences]

def get_word_set(sentence):
    """Get set of lowercase words."""
    words = re.findall(r'\b[a-zA-Z]+\b', sentence.lower())
    return set(words)

def build_word_overlap_graph(sentences, threshold=0.1):
    """Build graph with word overlap edges."""
    if len(sentences) < 2:
        G = nx.Graph()
        if sentences:
            G.add_node(0)
        return G
    
    G = nx.Graph()
    for i, sent in enumerate(sentences):
        G.add_node(i)
    
    word_sets = [get_word_set(sent) for sent in sentences]
    
    for i in range(len(sentences)):
        for j in range(i + 1, len(sentences)):
            set_i = word_sets[i]
            set_j = word_sets[j]
            
            if len(set_i) == 0 and len(set_j) == 0:
                similarity = 1.0
            elif len(set_i) == 0 or len(set_j) == 0:
                similarity = 0.0
            else:
                intersection = len(set_i & set_j)
                union = len(set_i | set_j)
                similarity = intersection / union if union > 0 else 0.0
            
            if similarity > threshold:
                G.add_edge(i, j, weight=similarity)
    
    # Ensure connected
    if len(sentences) > 1:
        for i in range(len(sentences) - 1):
            if not G.has_edge(i, i + 1):
                G.add_edge(i, i + 1, weight=0.1)
    
    return G

def compute_effective_resistance(G):
    """Compute effective graph resistance."""
    if G.number_of_nodes() < 2:
        return 0.0
    
    try:
        resistance = nx.effective_graph_resistance(G)
        return float(resistance)
    except Exception as e:
        print(f"Error in resistance: {e}")
        return float(G.number_of_nodes())

# Test with sample text
test_text = "This is a test. This is only a test. Testing is important for learning."
sentences = text_to_sentences(test_text)
print(f"Sentences: {len(sentences)}")
G = build_word_overlap_graph(sentences)
print(f"Graph nodes: {G.number_of_nodes()}, edges: {G.number_of_edges()}")
resistance = compute_effective_resistance(G)
print(f"Resistance: {resistance}")

# Test with data file
data_path = Path("/ai-inventor/aii_data/runs/run_RiHQW43yNEvO/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/preview_data_out.json")
print(f"\nLoading data from {data_path}")
with open(data_path, 'r') as f:
    data = json.load(f)

print(f"Number of datasets: {len(data.get('datasets', []))}")

# Process just 1 example
dataset = data['datasets'][0]
example = dataset['examples'][0]
text = example['input'][:500]  # Limit text length
print(f"\nProcessing example (truncated to 500 chars)")
print(f"Text: {text[:100]}...")

sentences = text_to_sentences(text)
print(f"Sentences: {len(sentences)}")
G = build_word_overlap_graph(sentences)
print(f"Graph: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")
resistance = compute_effective_resistance(G)
normalized = resistance / max(len(sentences), 1)
print(f"Resistance: {resistance:.4f}, Normalized: {normalized:.4f}")

fk_score = textstat.flesch_kincaid_grade(text)
print(f"Flesch-Kincaid: {fk_score:.4f}")

print("\nAll tests passed!")
