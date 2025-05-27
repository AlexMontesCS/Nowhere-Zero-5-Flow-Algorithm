import networkx as nx
import time
from nowhere_zero_flow import find_nowhere_zero_5_flow
import os

def is_bridgeless_cubic(G):
    return (
        nx.is_connected(G)
        and all(d == 3 for _, d in G.degree())
        and nx.edge_connectivity(G) >= 2
    )

def run_all_g6_tests():
    results = [] 
    for n in range(4, 17, 2):
        filename = f"./graphs/cubic{n}_bridgeless.g6"
        if not os.path.exists(filename):
            print(f"Skipping n={n}: file {filename} not found.")
            continue

        with open(filename, "r") as f:
            graphs = [nx.from_graph6_bytes(line.strip().encode()) for line in f]

        total = 0
        successes = 0
        total_time = 0
        max_flow = 0

        for G in graphs:
            if not is_bridgeless_cubic(G):
                continue
            total += 1
            try:
                start = time.time()
                flow, _ = find_nowhere_zero_5_flow(G)
                elapsed = (time.time() - start) * 1000  # ms
                successes += 1
                total_time += elapsed
                max_flow = max(max_flow, max(abs(v) for v in flow.values()))
            except Exception as e:
                print(f"Failure on graph with {len(G)} vertices: {e}")
                print(nx.to_graph6_bytes(G).decode().strip())
                continue


        if total == 0:
            continue

        avg_time = round(total_time / successes, 1) if successes else 0
        success_rate = f"{round((successes / total) * 100)}%"
        results.append((n, total, avg_time, max_flow, success_rate))

    # Output LaTeX table
    print("\\begin{tabular}{crrrr}")
    print("\\toprule")
    print("Vertices & \\# Graphs & Avg Time (ms) & Max Flow & Success Rate \\\\ ")
    print("\\midrule")
    for row in results:
        print(f"{row[0]} & {row[1]} & {row[2]} & {row[3]} & {row[4]} \\\\ ")
    print("\\bottomrule")
    print("\\end{tabular}")

if __name__ == "__main__":
    run_all_g6_tests()
