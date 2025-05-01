import heapq  # Used for priority queue (min-heap)

# Heuristic function: Manhattan Distance
# Calculates how far each tile is from its goal position
def heuristic(board, goal):
    distance = 0
    for i in range(3):          # Loop through each cell in the current board
        for j in range(3):
            val = board[i][j]   # Get the value at position (i, j)
            if val:             # Skip the blank tile (0)
                for x in range(3):          # Find the position of 'val' in the goal board
                    for y in range(3):
                        if goal[x][y] == val:
                            # Add the Manhattan distance to total
                            distance += abs(i - x) + abs(j - y)
    return distance

# Find the position of the blank tile (0) in the board
def find_blank(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return i, j  # Return coordinates of the blank tile

# Move the blank tile in the given direction, if possible
def move_blank(board, direction):
    i, j = find_blank(board)  # Find current blank tile position
    new_board = [row[:] for row in board]  # Create a deep copy of the board
    
    # Try to move blank tile in the specified direction by swapping tiles
    if direction == "up" and i > 0:
        new_board[i][j], new_board[i-1][j] = new_board[i-1][j], new_board[i][j]
    elif direction == "down" and i < 2:
        new_board[i][j], new_board[i+1][j] = new_board[i+1][j], new_board[i][j]
    elif direction == "left" and j > 0:
        new_board[i][j], new_board[i][j-1] = new_board[i][j-1], new_board[i][j]
    elif direction == "right" and j < 2:
        new_board[i][j], new_board[i][j+1] = new_board[i][j+1], new_board[i][j]
    else:
        return None  # Move not possible (e.g., trying to go up at top row)
    
    return new_board  # Return the new board state after the move

# A* Search Algorithm to solve the 8-puzzle problem
def a_star(start, goal):
    queue = []        # Priority queue to store nodes based on f = g + h
    visited = set()   # Set to keep track of visited board states (to avoid cycles)
    
    h = heuristic(start, goal)  # Initial heuristic value
    # Push initial state into queue: (f, g, board, path)
    heapq.heappush(queue, (h, 0, start, []))
    
    while queue:
        # Get the node with the lowest f (total cost) value
        f, g, board, path = heapq.heappop(queue)
        
        # If current board is the goal, print result and return
        if board == goal:
            print("Solved in", g, "moves.")
            print("Path:", path)
            return
        
        # Mark the current board as visited
        board_tup = tuple(tuple(row) for row in board)  # Convert board to hashable tuple
        visited.add(board_tup)
        
        # Try all possible directions to move the blank tile
        for move in ["up", "down", "left", "right"]:
            new_board = move_blank(board, move)
            
            if new_board is not None:
                new_board_tup = tuple(tuple(row) for row in new_board)
                if new_board_tup not in visited:
                    new_g = g + 1  # Increase path cost
                    new_h = heuristic(new_board, goal)  # Recalculate heuristic
                    new_f = new_g + new_h  # Total cost f = g + h
                    # Push the new state into the priority queue
                    heapq.heappush(queue, (new_f, new_g, new_board, path + [move]))
    
    # If queue is empty and goal was not found
    print("No Solution Found.")

# ---------------------
# Define the initial and goal board states

start = [[1, 2, 3],
         [4, 0, 5],
         [6, 7, 8]]   # Initial board

goal = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]]     # Goal board

# Testing individual components
print("Initial Heuristic Value:", heuristic(start, goal))  # Show heuristic value
print("Blank Tile Position:", find_blank(start))           # Show blank position
print("Move Blank Down:", move_blank(start, "down"))       # Try a sample move

# Solve the puzzle using A* search
a_star(start, goal)
