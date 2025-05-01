 # Disjoint Set Union (Union-Find) - used to detect cycles efficiently

# Find function with path compression
# This helps to find the root of a node's set quickly
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])  # Recursively set parent[x] to its root (path compression)
    return parent[x]

# Union function to merge two sets
# Returns True if two different sets were merged (i.e., no cycle), otherwise False
def union(x, y):
    rootX = find(x)
    rootY = find(y)
    if rootX != rootY:  # If they are in different sets
        parent[rootY] = rootX  # Merge the sets by pointing root of y to root of x
        return True
    return False  # Same set, adding this edge would create a cycle

# Graph represented as an adjacency list
# Each node points to a list of [neighbor, weight] pairs
graph = {
    "A": [["B", 1], ["D", 4]],
    "B": [["A", 1], ["E", 2], ["C", 3]],
    "C": [["B", 3], ["F", 5]],
    "D": [["A", 4], ["E", 6]],
    "E": [["B", 2], ["D", 6], ["F", 7]],
    "F": [["C", 5], ["E", 7]]
}

# Initialize each node to be its own parent
# This sets up the disjoint sets for the union-find operations
parent = {
    'A': 'A',
    'B': 'B',
    'C': 'C',
    'D': 'D',
    'E': 'E',
    'F': 'F'
}

# Step 1: Extract all unique edges from the graph
# Since the graph is undirected, we only add one direction (e.g., A-B, not both A-B and B-A)
edges = []
for u in graph:
    for v, weight in graph[u]:
        if u < v:  # This avoids adding duplicate edges (like A-B and B-A)
            edges.append([u, v, weight])

# Step 2: Sort edges in non-decreasing order of their weights
# Kruskal’s algorithm always picks the smallest edge first
edges.sort(key=lambda x: x[2])
print("Sorted edges by weight:", edges)

# Step 3: Initialize variables for the MST
mst = []   # To store edges in the final Minimum Spanning Tree
cost = 0   # Total weight (cost) of the MST

# Step 4: Process each edge in increasing order of weight
# If adding the edge doesn't form a cycle, include it in the MST
for u, v, weight in edges:
    if union(u, v):  # Only add if it doesn't create a cycle
        mst.append([u, v, weight])  # Add edge to MST
        cost += weight              # Add edge weight to total cost

# Final output
print("Minimum Spanning Tree:", mst)
print("Total cost of MST:", cost)
