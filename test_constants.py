"""
Test suite for HAGI Constants
"""

import pytest
import numpy as np
import networkx as nx
from constants import *

class TestDynamicCoherence:
    def test_empty_graph(self):
        G = nx.Graph()
        assert measure_dynamic_coherence(G) == 0.0
        
    def test_no_contradictions(self):
        G = nx.Graph()
        G.add_nodes_from([(1, {'label': 'cat'}), (2, {'label': 'dog'})])
        coherence = measure_dynamic_coherence(G)
        assert 0 <= coherence <= 1
        
    def test_with_contradictions(self):
        G = nx.Graph()
        G.add_nodes_from([
            (1, {'label': 'true'}),
            (2, {'label': 'false'}),  # Contradiction
            (3, {'label': 'maybe'})
        ])
        coherence = measure_dynamic_coherence(G)
        assert coherence > 0  # Should detect some contradiction

class TestPerceptualFidelity:
    def test_identical_arrays(self):
        data = np.random.rand(32, 32)
        fidelity_loss = measure_perceptual_fidelity(data, data)
        assert abs(fidelity_loss) < 1e-10
        
    def test_different_arrays(self):
        original = np.random.rand(16, 16)
        reconstructed = np.random.rand(16, 16)
        fidelity_loss = measure_perceptual_fidelity(original, reconstructed)
        assert fidelity_loss > 0.1

class TestInferentialDepth:
    def test_empty_chains(self):
        assert measure_inferential_depth([], [1, 0, 1]) == 0
        
    def test_short_reliable_chains(self):
        chains = [[1, 2, 3], [4, 5], [6]]  # Mock reasoning steps
        ground_truth = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
        depth = measure_inferential_depth(chains, ground_truth)
        assert depth >= 1

class TestResourceEfficiency:
    def test_perfect_efficiency(self):
        system_costs = [1.0, 2.0, 3.0]
        baseline_costs = [1.0, 2.0, 3.0]
        efficiency = measure_resource_efficiency(system_costs, baseline_costs)
        assert efficiency == 1.0
        
    def test_improved_efficiency(self):
        system_costs = [0.5, 1.0, 1.5]  # Better than baseline
        baseline_costs = [1.0, 2.0, 3.0]
        efficiency = measure_resource_efficiency(system_costs, baseline_costs)
        assert efficiency >= 2.0  # 2x improvement in worst case

class TestAdaptiveGenerality:
    def test_perfect_retention(self):
        before = {'task1': 0.9, 'task2': 0.8}
        after = {'task1': 0.9, 'task2': 0.8}
        generality = measure_adaptive_generality(before, after)
        assert generality == 1.0
        
    def test_catastrophic_forgetting(self):
        before = {'task1': 0.9, 'task2': 0.8}
        after = {'task1': 0.9, 'task2': 0.1}  # Forgot task2
        generality = measure_adaptive_generality(before, after)
        assert generality < 0.2

class TestConceptualStability:
    def test_identical_embeddings(self):
        emb = np.random.rand(10)
        embeddings = [emb, emb.copy()]
        perturbations = [emb, emb.copy()]
        stability = measure_conceptual_stability(embeddings, perturbations)
        assert abs(stability - 1.0) < 1e-10
        
    def test_different_embeddings(self):
        embeddings = [np.random.rand(5) for _ in range(3)]
        perturbations = [np.random.rand(5) for _ in range(3)]
        stability = measure_conceptual_stability(embeddings, perturbations)
        assert stability < 0.5

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
