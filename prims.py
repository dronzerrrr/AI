
# Function to find the minimum cost edge from the visited set to an unvisited node
def find_min_edge(visited):
    min_cost = 99999   # Initialize with a very high cost
    min_edge = ()      # To store the minimum cost edge
    for j in visited:  # Iterate over visited nodes
        for i in graph[j]:  # Check all edges from the visited node
            if i[1] < min_cost and i[0] not in visited: 
                # If the neighbor is not visited and cost is less than current min
                min_cost = i[1]
                min_edge = i  # Store this edge
                src = j       # Store source node for printing
                dest = i[0]   # Store destination node (not used further)
                
    print(src, "->", min_edge)  # Print the selected edge
    return min_edge             # Return the edge (destination, cost)

# Function to implement Prim's algorithm
def Prims():
    visited = []   # List to keep track of visited nodes
    cost = 0       # Total cost of the Minimum Spanning Tree
    visited.append("A")  # Starting node is 'A'
    
    # Loop until all nodes are visited
    while len(visited) != len(graph.keys()):
        min_edge = find_min_edge(visited)  # Find the smallest edge to unvisited node
        if len(min_edge):                  # If a valid edge is found
            visited.append(min_edge[0])   # Add the new node to visited
            cost += min_edge[1]           # Add the edge cost to total
    
    print("Total Cost : ", cost)  # Print the total cost of the MST
            

# Graph definition
graph = {
    "A": [["B", 2], ["C", 3]],
    "B": [["A", 2], ["D", 1]],
    "C": [["A", 3], ["D", 4]],
    "D": [["B", 1], ["C", 4]]
}

# Run Prim's algorithm with 'A' as starting node
Prims()


