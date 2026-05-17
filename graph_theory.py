import random

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
# STEP 6: Run the program
# Generate a graph, check connectivity, print results
# Run it 5 times to show different random graphs
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