# Nowhere-Zero 5-Flows in Cubic Bidirected Graphs: A Constructive Approach

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) Welcome to the official implementation of the research paper: **"Nowhere-Zero 5-Flows in Cubic Bidirected Graphs: A Constructive Approach via Perfect Matchings"** by Alexander J. Montes (Rutgers University, May 30, 2025).

This project provides Python code to constructively find nowhere-zero 5-flows in bridgeless cubic bidirected graphs, a result that improves upon the general 6-flow bound predicted by Bouchet's conjecture for this important class of graphs.

## 🌟 Overview

The theory of nowhere-zero flows is a cornerstone of modern graph theory. This work tackles a key conjecture in this area for *bidirected graphs*—graphs where each end of an edge has its own orientation (sign).

This research introduces:
* A **theoretical improvement**: Proving that every bridgeless cubic bidirected graph admits a nowhere-zero 5-flow. A $k$-flow requires flow values on edges to be non-zero integers with absolute value less than $k$. For our 5-flows, this means flow values $f(e) \in \{\pm1, \pm2, \pm3, \pm4\}$.
* A **constructive algorithm**: An explicit, polynomial-time algorithm to find these 5-flows. The worst-case deterministic running time is $O(|V|^7)$.
* A **novel framework**: Recasting the flow problem as finding short vectors in an integer lattice (the flow lattice), leveraging the power of lattice reduction techniques like LLL.

This repository contains a Python implementation of this constructive algorithm, allowing for experimentation and verification of the paper's findings.

## 💡 Key Concepts

* **Bidirected Graphs**: Graphs where each edge endpoint has a sign ($\pm 1$), indicating if the edge is "incoming" or "outgoing" relative to that endpoint.
* **Nowhere-Zero k-Flow**: An assignment of integer flow values to edges such that Kirchhoff's law (flow conservation) holds at every vertex, and no edge has zero flow, with all flow values $f(e)$ satisfying $0 < |f(e)| < k$.
* **Flow Lattice ($\Lambda(G)$)**: The set of all valid integer flows on a graph forms an integer lattice, specifically the integer kernel of the signed incidence matrix $B$ ($\text{ker}_{\mathbb{Z}}B$).
* **LLL Algorithm**: A polynomial-time lattice reduction algorithm used here to find a "good" basis for the flow lattice, consisting of relatively short vectors.

## 🛠️ The Algorithm Implemented

The core approach implemented here, based on Algorithm 1 in the paper, is:
1.  **Input**: A bridgeless cubic graph $G=(V,E)$.
2.  **Bidirect it**: Construct a signed incidence matrix $B$ for $G$, effectively assigning bidirections to its edges.
3.  **Flow Lattice Basis**: Compute an initial integer basis for the flow lattice $\Lambda(G) = \text{ker}_{\mathbb{Z}}B$. (The provided code uses `sympy.nullspace()` for this step).
4.  **LLL Reduction**: Apply the LLL algorithm (with $\delta=3/4$) to the initial basis to obtain a reduced basis $\{g_1, \dots, g_\beta\}$.
5.  **Coefficient Enumeration**: Search for a coefficient vector $(a_1, \dots, a_\beta)$ with small integer entries (the code tests $a_i \in [-A, A]$ for $A=1,2,3,4$).
6.  **Construct Flow**: Compute $f = \sum a_i g_i$. The first non-zero $f$ found where all edge flows $f(e)$ are in $\{\pm1, \pm2, \pm3, \pm4\}$ is our nowhere-zero 5-flow.

## 🐍 What The Code Does

This Python implementation includes:
* `generate_random_cubic_graph`: Generates random connected, bridgeless cubic graphs for testing.
* `create_signed_incidence_matrix`: Constructs the signed incidence matrix $B$ for a given graph, assigning random valid bidirections.
* `compute_flow_basis_direct`: Computes an integer basis for the kernel of $B$ using `sympy`.
* `apply_LLL_reduction`: Applies LLL basis reduction using the `fpylll` library.
* `enumerate_nowhere_zero_flows`: Searches for a linear combination of LLL-reduced basis vectors that constitutes a nowhere-zero 5-flow with edge values in $\{\pm1, \dots, \pm4\}$.
* `run_comprehensive_tests`: A script to run experiments on various graphs (including $K_4$, Petersen graph, random cubic graphs), collect statistics (success rate, average time, coefficient bounds needed), and format them for inclusion in Section 4 of the paper.

## 🚀 Getting Started

### Dependencies
You'll need the following Python libraries:
* `networkx`
* `numpy`
* `sympy`
* `fpylll`

You can typically install them using pip:
```bash
pip install networkx numpy sympy fpylll
```

### Running the Tests
The main script to demonstrate the algorithm and generate results is `main.py`
To run the comprehensive tests which will output a results table:
```bash
python main.py
```
This will execute the `run_comprehensive_tests()` function.

## 📜 Citing the Research

If you use concepts or findings from this research, please cite the paper:

Montes, Alexander J. "Nowhere-Zero 5-Flows in Cubic Bidirected Graphs: A Constructive Approach via Perfect Matchings." Rutgers University, May 30, 2025.

## 🔮 Future Directions

The paper explores several exciting avenues for future research, including:
* Extending these lattice-reduction techniques to general $r$-regular graphs  or irregular graphs.
* Making further progress towards Bouchet's 6-flow conjecture for all bidirected graphs.
* Algorithmic improvements, such as parallel implementations or using different lattice reduction techniques (e.g., BKZ).

---

Feel free to explore the code, run experiments, and contribute! This work demonstrates the power of combining structural graph theory with algorithmic techniques from lattice theory.
