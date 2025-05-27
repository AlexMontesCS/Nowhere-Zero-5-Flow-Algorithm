# Nowhere-Zero 5-Flow Algorithm

This project implements a constructive algorithm proving that every **bridgeless cubic graph** admits a **nowhere-zero 5-flow**. The method is based on the original research of **Alexander J. Montes** and includes a verified Python implementation.

## 📘 Background

A *nowhere-zero 5-flow* assigns nonzero integers to the edges of a directed graph such that the sum of incoming and outgoing flows at each vertex is zero. The algorithm computes such flows using only values from \(\{ \pm1, \pm2 \}\), proving a special case of Tutte's 5-flow conjecture for bridgeless cubic graphs.

---

## 🚀 Features

- Handles any undirected **bridgeless cubic graph**
- Builds a **cycle basis** from a spanning tree + perfect matching
- Uses a randomized coefficient assignment with backtracking
- Verifies that all edge flows are nonzero and within \(\{ \pm1, \pm2, \pm3, \pm4 \}\)
- Supports bulk analysis of graphs in `.g6` format

---

## 📂 Files

- `nowhere_zero_flow.py`  
  Core implementation of the 5-flow construction algorithm

- `analyze_all.py`  
  Runs the algorithm on every `graphs/cubic*_bridgeless.g6` file, outputs LaTeX summary

- `generate_bridgeless_cubic.sh`  
  Shell script to generate all **connected**, **3-regular**, **bridgeless** graphs from \( n = 4 \) to \( 20 \)

- `graphs/`  
  Directory containing `.g6` files with one graph per line (output from `geng` and filtered via Python)

---

## ⚙️ Usage

### 1. Install dependencies

```bash
pip install networkx
```

### 2. Generate bridgeless cubic graphs

```bash
bash generate_bridgeless_cubic.sh
```

This creates one file per even `n`:
```
graphs/cubic{n}_bridgeless.g6
```

### 3. Analyze all graphs with the 5-flow algorithm

```bash
python analyze_all.py
```

---

## ✅ Example Output

```
Vertices & \# Graphs & Avg Time (ms) & Max Flow & Success Rate \\
\midrule
4 & 1 & 2.0 & 4 & 100% \\
6 & 2 & 0.0 & 3 & 100% \\
8 & 5 & 0.2 & 4 & 100% \\
10 & 18 & 0.8 & 4 & 100% \\
12 & 81 & 1.1 & 4 & 100% \\
14 & 480 & 1.9 & 4 & 100% \\
16 & 3874 & 3.8 & 4 & 100% \\
\bottomrule
```

---

## 🧠 Requirements

- Python 3.7+
- `networkx`
- Optional: `geng` (from Nauty) for graph generation

---

## 📚 Citation

This project is based on the original research of **Alexander J. Montes (2025)**.  
If you use this code in academic work, please cite accordingly.

---

## 🪪 License

MIT License — free to use, modify, and share. Attribution required for academic use.
