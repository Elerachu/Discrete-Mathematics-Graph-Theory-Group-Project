# Discrete Mathematics — Euler Circuit Project

A Python program that randomly generates simple undirected graphs with 10 vertices, checks whether each graph is connected, detects the presence of an Euler circuit, outputs the circuit path when one exists, and estimates the probability of a connected graph having an Euler circuit through Monte Carlo simulation.

---

## Team Members

| Member | Responsibility |
|--------|---------------|
| Elera Obari Josiah-Chu | Graph generation and connectivity checking |
| Nellyvine Tako Mizero | Euler circuit detection and path finding |
| Hanif Olayiwola | Probability estimation and document assembly |

---

## What the Program Does

1. Generates a random simple undirected graph with 10 vertices (A through J)
2. Checks whether the graph is connected using Depth First Search (DFS)
3. Calculates the degree of every vertex
4. Determines whether an Euler circuit exists (Euler's theorem: all vertices must have even degree)
5. Finds and outputs the Euler circuit path using Hierholzer's Algorithm if one exists
6. Runs 10,000 simulation trials to estimate the probability that a connected graph has an Euler circuit

---

## Key Concepts

**Simple undirected graph** — a graph where edges have no direction and no vertex connects to itself, with at most one edge between any pair of vertices.

**Graph connectivity** — a graph is connected if there is a path between every pair of vertices.

**Euler circuit** — a closed trail that visits every edge in the graph exactly once and returns to the starting vertex.

**Euler's Theorem** — a connected graph has an Euler circuit if and only if every vertex has an even degree.

**Hierholzer's Algorithm** — an efficient algorithm for constructing an Euler circuit in O(E) time, where E is the number of edges.

**Monte Carlo simulation** — a method of estimating probability by running a large number of random trials and measuring the frequency of an outcome.

---

## How to Run

No external libraries are required. The program uses only Python's built-in `random` and `copy` modules.

```bash
python main.py
```

The program will:
- Run 5 random graph examples and print results for each
- Run a sanity check on a known square graph
- Run the Monte Carlo simulation twice and print the probability estimate

---

## Sample Output

```
=======================================================
  Random Graph Generator — 10 Vertices
=======================================================

--- Run 1 ---
Edge list: (A,B), (A,D), (B,C), (C,E), (D,E), (E,F)
Number of edges: 6
Graph is connected: Yes

Vertex degrees:
  Vertex A: degree 2
  Vertex B: degree 2
  ...

Euler Circuit exists: Yes
Euler Circuit: A → B → C → E → D → A

=======================================================
  Monte Carlo Simulation — 10,000 Iterations
=======================================================

--- Run 1 of 2 ---
  Total graphs generated             :  10,000
  Connected graphs                   :   9,796
  Connected graphs with Euler circuit:      18
  Estimated probability              :  0.0018

--- Run 2 of 2 ---
  Total graphs generated             :  10,000
  Connected graphs                   :   9,811
  Connected graphs with Euler circuit:      24
  Estimated probability              :  0.0024

  Difference between runs: 0.0006
  Estimate stable? Yes
```

---

## Estimated Probability

**P(Euler circuit | connected) ≈ 0.0021**

Across two independent runs of 10,000 iterations each, approximately 2 in every 1,000 connected simple graphs with 10 vertices contained an Euler circuit. The even-degree condition is a strict constraint that random graphs rarely satisfy across all vertices simultaneously, which explains how low this probability is.

---

## Project Documentation

The full written documentation explaining the Discrete Mathematics concepts, code walkthrough, and probability analysis is available here: [https://docs.google.com/document/d/1bEJmh2EltG5_DtdKBlRRSmqY-iOwQGFMvDlDTrPIUnI/edit?tab=t.0]

---

## File Structure

```
├── main.py        # Full combined program (all three members)
└── README.md      # This file
```
