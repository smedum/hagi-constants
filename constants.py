"""
HAGI Constants Reference Implementation
Six mathematical constants for harmonious intelligence
"""

import numpy as np
from scipy.spatial.distance import cosine
from sklearn.metrics import accuracy_score
import networkx as nx
from typing import Dict, List, Any, Union

def measure_dynamic_coherence(knowledge_graph: nx.Graph) -> float:
    """
    Measures δ: Approximation of logical contradiction density.
    Practical implementation using node attribute analysis.
    """
    if len(knowledge_graph.nodes) == 0:
        return 0.0
    
    contradiction_score = 0.0
    nodes = list(knowledge_graph.nodes(data=True))
    
    for i, (node1, data1) in enumerate(nodes):
        for j, (node2, data2) in enumerate(nodes[i+1:], i+1):
            if _nodes_contradict(node1, data1, node2, data2):
                contradiction_score += 1
                
    total_pairs = len(nodes) * (len(nodes) - 1) / 2
    return contradiction_score / total_pairs if total_pairs > 0 else 0.0

def measure_perceptual_fidelity(original: np.ndarray, reconstructed: np.ndarray) -> float:
    """
    Measures γ: Multi-scale distortion metric.
    Combines pixel-level and structural similarity.
    """
    # Mean squared error (preserves strict 0 for identity)
    mse = np.mean((original - reconstructed) ** 2)
    
    # Structural similarity (handles perceptual quality)
    if original.ndim >= 2:
        try:
            from skimage.metrics import structural_similarity
            data_range = original.max() - original.min()
            ssim = structural_similarity(original, reconstructed, data_range=data_range)
            # Combine metrics (weighted toward stricter MSE)
            return 0.7 * mse + 0.3 * (1 - ssim)
        except:
            pass
    
    return mse

def measure_inferential_depth(reasoning_chains: List[List[Any]], 
                            ground_truth: List[Any]) -> int:
    """
    Measures ι: Maximum reliable reasoning chain length.
    Chains are lists of reasoning steps.
    """
    if not reasoning_chains:
        return 0
        
    max_reliable_depth = 0
    accuracy_threshold = 0.95  # η
    
    for chain in reasoning_chains:
        if not chain:
            continue
            
        # Simple implementation: accuracy decreases with chain length
        predictions = _simulate_reasoning_chain(chain)
        if len(predictions) != len(ground_truth):
            continue
            
        accuracy = accuracy_score(ground_truth, predictions)
        reliability_factor = 1.0 - (0.1 * len(chain))  # 10% decay per step
        
        if accuracy * reliability_factor >= accuracy_threshold:
            max_reliable_depth = max(max_reliable_depth, len(chain))
    
    return max_reliable_depth

def measure_resource_efficiency(system_costs: List[float], 
                              baseline_costs: List[float]) -> float:
    """
    Measures ρ: Worst-case resource efficiency ratio.
    Lower bound on performance across tasks.
    """
    if not system_costs or not baseline_costs:
        return 0.0
        
    ratios = []
    for system_cost, baseline_cost in zip(system_costs, baseline_costs):
        if system_cost > 0 and baseline_cost > 0:
            efficiency = baseline_cost / system_cost
            ratios.append(efficiency)
    
    return min(ratios) if ratios else 0.0

def measure_adaptive_generality(performance_before: Dict[str, float],
                              performance_after: Dict[str, float]) -> float:
    """
    Measures α: Worst-case knowledge retention after learning.
    """
    if not performance_before:
        return 0.0
        
    retention_scores = []
    for task, perf_before in performance_before.items():
        perf_after = performance_after.get(task, 0.0)
        if perf_before > 0:
            retention = perf_after / perf_before
            retention_scores.append(retention)
    
    return min(retention_scores) if retention_scores else 0.0

def measure_conceptual_stability(original_embeddings: List[np.ndarray],
                               perturbed_embeddings: List[np.ndarray]) -> float:
    """
    Measures σ: Worst-case stability under perturbation.
    Lower bound on cosine similarity across all examples.
    """
    if not original_embeddings:
        return 0.0
        
    similarities = []
    for orig, pert in zip(original_embeddings, perturbed_embeddings):
        if orig.shape == pert.shape and np.linalg.norm(orig) > 0 and np.linalg.norm(pert) > 0:
            similarity = 1 - cosine(orig, pert)
            similarities.append(similarity)
    
    return min(similarities) if similarities else 0.0

# Helper implementations
def _nodes_contradict(node1: Any, data1: dict, node2: Any, data2: dict) -> bool:
    """Check if two knowledge graph nodes contradict each other."""
    # Simple contradiction detection based on node attributes
    if 'label' in data1 and 'label' in data2:
        label1 = str(data1['label']).lower()
        label2 = str(data2['label']).lower()
        
        # Basic contradiction patterns
        contradictions = [
            ('true', 'false'), ('yes', 'no'), ('positive', 'negative'),
            ('exists', 'not_exists'), ('valid', 'invalid')
        ]
        
        for contr1, contr2 in contradictions:
            if (contr1 in label1 and contr2 in label2) or (contr2 in label1 and contr1 in label2):
                return True
                
    return False

def _simulate_reasoning_chain(chain: List[Any]) -> List[Any]:
    """Simulate reasoning chain execution - placeholder implementation."""
    # For testing, return random predictions correlated with chain length
    rng = np.random.RandomState(len(chain))  # Seed with chain length for reproducibility
    return rng.choice([0, 1], size=10)  # Binary classification example
