import networkx as nx
import numpy as np
from itertools import product
from random import choice

def is_valid_2_factor(G, M):
    # Fix: M is stored as sorted tuples, so compare sorted
    M_set = set(tuple(sorted(e)) for e in M)
    F_edges = [e for e in G.edges if tuple(sorted(e)) not in M_set]

    F_graph = nx.Graph()
    F_graph.add_edges_from(F_edges)

    return all(
        nx.is_connected(F_graph.subgraph(comp)) and
        all(d == 2 for _, d in F_graph.subgraph(comp).degree())
        for comp in nx.connected_components(F_graph)
    )

def get_valid_matching(G, trials=10):
    for _ in range(trials):
        M = nx.algorithms.matching.max_weight_matching(G, maxcardinality=True)
        M = set(map(lambda e: tuple(sorted(e)), M))
        if len(M) != G.number_of_nodes() // 2:
            continue
        if is_valid_2_factor(G, M):
            return M
    raise ValueError("No valid perfect matching found that gives a 2-factor")

def find_nowhere_zero_5_flow(G, max_trials=100000):
    if not nx.is_connected(G):
        raise ValueError("Graph must be connected.")
    if any(d != 3 for _, d in G.degree()):
        raise ValueError("Graph must be cubic (3-regular).")

    edge_list = list(map(tuple, map(sorted, G.edges())))
    edge_index = {e: i for i, e in enumerate(edge_list)}

    # Get the cycle basis
    basis_cycles = nx.cycle_basis(G)
    cycle_basis = np.zeros((len(basis_cycles), len(edge_list)), dtype=int)

    for i, cycle in enumerate(basis_cycles):
        edges = [(cycle[j], cycle[(j + 1) % len(cycle)]) for j in range(len(cycle))]
        for u, v in edges:
            idx = edge_index[tuple(sorted((u, v)))]
            cycle_basis[i, idx] = 1

    for _ in range(max_trials):
        coeffs = [choice([-2, -1, 1, 2]) for _ in range(len(basis_cycles))]
        flow = np.zeros(len(edge_list), dtype=int)
        for i in range(len(basis_cycles)):
            flow += coeffs[i] * cycle_basis[i]
        if np.all(flow != 0) and np.max(np.abs(flow)) <= 4:
            return dict(zip(edge_list, flow.tolist())), coeffs

    raise ValueError("No nowhere-zero 5-flow found.")
