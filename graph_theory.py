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


# ════════════════════════════════════════════════════════
#  PART A — Generate and analyse 5 random graphs
# ════════════════════════════════════════════════════════

print("=" * 55)
print("  Random Graph Generator — 10 Vertices")
print("=" * 55)
print()

for run in range(1, 6):
    print(f"--- Run {run} ---")

    edges     = generate_random_graph(vertices, probability=0.4)
    graph     = build_graph(vertices, edges)
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


# ════════════════════════════════════════════════════════
#  PART B — Sanity check on a known graph
#
#  We verify Hierholzer's algorithm on a square graph
#  (0–1–2–3–0) before trusting it on random graphs.
#  Every vertex has degree 2 (even), so an Euler circuit
#  must exist. Expected result: 0 → 1 → 2 → 3 → 0
# ════════════════════════════════════════════════════════

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

assert has_euler_circuit(test_degrees), "Test FAILED — square should be Eulerian"

test_circuit = find_euler_circuit(test_graph, test_vertices)
print("Sanity check passed:", " → ".join(test_circuit))
print("(Expected: 0 → 1 → 2 → 3 → 0)")
print()


# ════════════════════════════════════════════════════════
#  PART C — Monte Carlo probability estimation
#
#  We estimate P(Euler circuit | graph is connected).
#
#  Method:
#    Run 10,000 random graph trials.
#    For each trial:
#      — if the graph is not connected, skip it entirely
#        (a disconnected graph cannot have an Euler circuit
#         and must not count in the denominator)
#      — if connected, check for an Euler circuit
#
#    P(Euler | connected) = euler_count / connected_count
#
#  Why 10,000 iterations?
#    Euler circuits are rare (~0.1–0.2% of connected graphs).
#    With 10,000 trials roughly 9,000 are connected, giving
#    ~10–20 Euler cases — enough for a stable estimate.
#    We run the simulation twice and compare; if the two
#    results agree within 0.01, the sample size is sufficient.
# ════════════════════════════════════════════════════════

def run_simulation(iterations=10_000):
    total_generated      = 0
    total_connected      = 0
    connected_with_euler = 0

    for _ in range(iterations):
        edges = generate_random_graph(vertices, probability=0.4)
        graph = build_graph(vertices, edges)
        total_generated += 1

        if not is_connected(graph, vertices):
            continue                             # skip disconnected graphs entirely

        total_connected += 1
        degrees = get_degrees(graph)

        if has_euler_circuit(degrees):
            connected_with_euler += 1

    probability = (connected_with_euler / total_connected
                   if total_connected > 0 else 0.0)

    return total_generated, total_connected, connected_with_euler, probability


def print_simulation_summary(run_label, total, connected, euler, prob):
    print(f"--- {run_label} ---")
    print(f"  Total graphs generated             : {total:>7,}")
    print(f"  Connected graphs                   : {connected:>7,}")
    print(f"  Connected graphs with Euler circuit: {euler:>7,}")
    print(f"  Estimated P(Euler | connected)     : {prob:.4f}  (~{prob * 100:.2f}%)")
    print()


print("=" * 55)
print("  Monte Carlo Simulation — 10,000 Iterations")
print("=" * 55)
print()

t1, c1, e1, p1 = run_simulation()
print_simulation_summary("Run 1 of 2", t1, c1, e1, p1)

t2, c2, e2, p2 = run_simulation()
print_simulation_summary("Run 2 of 2", t2, c2, e2, p2)

diff = abs(p1 - p2)
print(f"  Difference between runs  : {diff:.4f}")
print(f"  Estimate stable?         : {'Yes' if diff < 0.01 else 'No — consider more iterations'}")
print()
print("  Interpretation:")
print(f"  Given that a random graph on 10 vertices (p=0.4) is")
print(f"  connected, there is approximately a {((p1+p2)/2)*100:.2f}% chance")
print(f"  it also contains an Euler circuit.")
print()
print("  Why so low?")
print("  For an Euler circuit to exist, ALL 10 vertices must")
print("  have even degree simultaneously. The probability that")
print("  any single vertex has even degree is roughly 0.5.")
print("  All 10 being even at once is approximately (0.5)^10")
print("  = 1/1024 ≈ 0.10%, consistent with our result.")
