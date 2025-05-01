# Define the graph using an adjacency list representation
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}

# Depth First Search (DFS) - Recursive implementation
def dfs(node, visit):
    print(node, end=' ')           # Print the current node
    visit.append(node)             # Mark the node as visited
    for i in graph[node]:          # Explore all adjacent nodes
        if i not in visit:         # If neighbor hasn't been visited, recurse
            dfs(i, visit)

print("Depth First Search : ", end=' ')
dfs("A", [])                       # Call DFS starting from node 'A'

# Breadth First Search (BFS) - Iterative implementation using a queue
print("\nBreadth First Search : ", end=' ')
que = []                           # Initialize the queue
visited = []                       # List to keep track of visited nodes
que.append("A")                    # Start BFS from node 'A'

while que:
    temp = que.pop(0)             # Dequeue a node
    print(temp, end=' ')          # Process (print) the current node
    visited.append(temp)          # Mark the node as visited
    for i in graph[temp]:         # Check all adjacent nodes
        # Enqueue if the node hasn't been visited and not already in queue
        if i not in visited and i not in que:
            que.append(i)
