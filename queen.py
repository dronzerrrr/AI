# Function to check whether it's safe to place a queen at board[row][col]
def isSafe(board, row, col, n):
    
    # Check the current row (left to right)
    for i in range(n):
        if board[row][i] == 'Q':
            return False

    # Check the current column (top to bottom)
    for i in range(n):
        if board[i][col] == 'Q':
            return False

    # Check upper-left diagonal
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i = row
    j = col
    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    # If no conflicts, position is safe
    return True

# Recursive function to solve the N-Queens problem using backtracking
def nQueens(board, row, n):
    # Base case: if all queens are placed, print the solution
    if row == n:
        for i in board:
            print(i)
        print()
        return

    # Try placing a queen in each column of the current row
    for j in range(n):
        if isSafe(board, row, j, n):
            # Place the queen if it's safe
            board[row][j] = 'Q'
            
            # Recurse for the next row
            nQueens(board, row + 1, n)

            # Backtrack: remove the queen and try next column
            board[row][j] = '.'

# Take input from the user for board size
n = int(input("Enter the size of the board (e.g., 8 for 8x8): "))

# Initialize the board with all cells empty ('.')
board = [["." for i in range(n)] for j in range(n)]

# Start solving from the first row
nQueens(board, 0, n)
