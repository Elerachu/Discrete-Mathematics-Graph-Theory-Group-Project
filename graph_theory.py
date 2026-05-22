import random
import copy

# ─────────────────────────────────────────────
# STEP 1: Define the 10 vertices
# ─────────────────────────────────────────────
vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']


# ─────────────────────────────────────────────
# STEP 2: Randomly generate edges
# Loop through every pair of vertices and randomly add edges.
# probability=0.4 means each pair has a 40% chance of being connected.
# ─────────────────────────────────────────────
def generate_random_graph(vertices, probability=0.4):
    edges = []

    for i in range(len(vertices)):
        for j in range(i + 1, len(vertices)):  # j starts at i+1 to avoid self-loops and duplicates
            if random.random() < probability:   # "flip a coin"
                edges.append((vertices[i], vertices[j]))

    return edges


# ─────────────────────────────────────────────
# STEP 3: Build an adjacency list from the edges
# An adjacency list stores each vertex's neighbours.
# Since the graph is undirected, every edge goes
# both ways: A-B means A sees B and B sees A.
# ─────────────────────────────────────────────
def build_graph(vertices, edges):
    graph = {v: [] for v in vertices}  # start with empty list for each vertex

    for edge in edges:
        graph[edge[0]].append(edge[1])  # add B to A's neighbours
        graph[edge[1]].append(edge[0])  # add A to B's neighbours (undirected)

    return graph


# ─────────────────────────────────────────────
# STEP 4: Check connectivity using DFS
# We start at the first vertex and follow edges
# to visit as many vertices as possible.
# If we visited all 10, the graph is connected.
# ─────────────────────────────────────────────
def is_connected(graph, vertices):
    visited = set()         # keep track of visited vertices
    stack = [vertices[0]]   # start DFS from vertex A

    while stack:
        vertex = stack.pop()                    # take the next vertex to visit

        if vertex not in visited:
            visited.add(vertex)                 # mark it as visited

            for neighbour in graph[vertex]:     # look at all its neighbours
                if neighbour not in visited:
                    stack.append(neighbour)     # add unvisited neighbours to the stack

    return len(visited) == len(vertices)        # True only if all vertices were visited


# ─────────────────────────────────────────────
# STEP 5: Print the graph clearly
# Show all edges in a readable format
# ─────────────────────────────────────────────
def print_graph(edges, connected):
    print("Edge list: ", end="")
    print(", ".join(f"({e[0]},{e[1]})" for e in edges))
    print(f"Number of edges: {len(edges)}")
    print(f"Graph is connected: {'Yes' if connected else 'No'}")
    print()


# ─────────────────────────────────────────────
# STEP 6: Calculate the degree of each vertex
# The degree of a vertex is the number of edges
# connected to it. We count its neighbours in
# the adjacency list — that gives the degree directly.
# ─────────────────────────────────────────────
def get_degrees(graph):
    degrees = {}

    for vertex in graph:
        degrees[vertex] = len(graph[vertex])    # number of neighbours = degree

    return degrees


# ─────────────────────────────────────────────
# STEP 7: Print all vertex degrees clearly
# ─────────────────────────────────────────────
def print_degrees(degrees):
    print("Vertex degrees:")
    for vertex, degree in degrees.items():
        print(f"  Vertex {vertex}: degree {degree}")
    print()


# ─────────────────────────────────────────────
# STEP 8: Check for an Euler circuit
# Euler's theorem: a connected graph has an Euler
# circuit if and only if EVERY vertex has even degree.
# If any vertex has an odd degree, return False.
# ─────────────────────────────────────────────
def has_euler_circuit(degrees):
    for vertex in degrees:
        if degrees[vertex] % 2 != 0:           # odd degree found
            return False

    return True                                 # all even → Euler circuit exists


# ─────────────────────────────────────────────
# STEP 9: Find the Euler circuit using Hierholzer's Algorithm
#
# How it works:
# 1. Start at any vertex and push it onto a stack.
# 2. If the top vertex still has unused edges, follow
#    one and remove it so it cannot be used again.
# 3. If the top vertex has no more unused edges,
#    pop it off and add it to the circuit.
# 4. Repeat until the stack is empty.
# 5. Reverse the result — Hierholzer's builds the
#    path backwards, so reversing gives the correct
#    forward traversal starting from vertex A.
#
# We use a deep copy of the graph so the original
# adjacency list is not modified during the search.
# ─────────────────────────────────────────────
def find_euler_circuit(graph, vertices):
    temp_graph = copy.deepcopy(graph)           # work on a copy, not the original

    start = vertices[0]                         # start from vertex A
    stack = [start]
    circuit = []

    while stack:
        v = stack[-1]                           # look at the top of the stack

        if temp_graph[v]:                       # if v still has unused edges
            u = temp_graph[v][0]                # pick the first available neighbour
            stack.append(u)                     # push neighbour onto the stack
            temp_graph[v].remove(u)             # remove edge v–u
            temp_graph[u].remove(v)             # remove reverse edge u–v (undirected)

        else:
            circuit.append(stack.pop())         # no edges left from v → add to circuit

    circuit.reverse()                           # Hierholzer's builds in reverse — fix the order
    return circuit


# ─────────────────────────────────────────────
# STEP 10: Print the Euler circuit result clearly
# ─────────────────────────────────────────────
def print_euler_result(has_circuit, circuit=None):
    print(f"Euler Circuit exists: {'Yes' if has_circuit else 'No'}")

    if has_circuit and circuit:
        path = " → ".join(circuit)
        print(f"Euler Circuit: {path}")
    else:
        print("(Not all vertices have even degree — no Euler circuit is possible.)")

    print()


# ─────────────────────────────────────────────
# STEP 11: Run the program
# Generate a graph, check connectivity and Euler circuit.
# Run it 5 times to show different random graphs.
# ─────────────────────────────────────────────
print("=" * 55)
print("  Random Graph Generator — 10 Vertices")
print("=" * 55)
print()

for run in range(1, 6):
    print(f"--- Run {run} ---")

    edges = generate_random_graph(vertices, probability=0.4)
    graph = build_graph(vertices, edges)
    connected = is_connected(graph, vertices)

    print_graph(edges, connected)

    degrees = get_degrees(graph)
    print_degrees(degrees)

    if not connected:
        print("Euler Circuit exists: No")
        print("(Graph is not connected — Euler circuit requires a connected graph.)")
        print()
    else:
        euler = has_euler_circuit(degrees)
        if euler:
            circuit = find_euler_circuit(graph, vertices)
            print_euler_result(True, circuit)
        else:
            print_euler_result(False)


# ─────────────────────────────────────────────
# STEP 12: Sanity check — verify Hierholzer's
# algorithm on a known graph before trusting it
# on random graphs.
#
# A square (0-1-2-3-0) has 4 vertices each with
# degree 2 (even), so an Euler circuit must exist.
# Expected circuit: 0 → 1 → 2 → 3 → 0
# ─────────────────────────────────────────────
print("=" * 55)
print("  Sanity Check — Square Graph (0-1-2-3-0)")
print("=" * 55)
print()

test_vertices = ['0', '1', '2', '3']
test_edges    = [('0','1'), ('1','2'), ('2','3'), ('3','0')]
test_graph    = build_graph(test_vertices, test_edges)
test_degrees  = get_degrees(test_graph)

print("Edge list: (0,1), (1,2), (2,3), (3,0)")
print("Vertex degrees:")
for v, d in test_degrees.items():
    print(f"  Vertex {v}: degree {d}")
print()

assert has_euler_circuit(test_degrees), "Test failed: square should be Eulerian"

test_circuit = find_euler_circuit(test_graph, test_vertices)
print("Sanity check passed:", " → ".join(test_circuit))
print("(Expected: 0 → 1 → 2 → 3 → 0)")
