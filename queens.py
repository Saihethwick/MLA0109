def is_safe(board, row, col):
    # Check if there is a queen in the same column up to the current row
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_queens(board, row):
    n = len(board)
    if row == n:  # Base case: all queens are placed
        return True

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            if solve_queens(board, row + 1):  # Recur to place queens in the next row
                return True
            board[row] = -1  # Backtrack if placing a queen at (row, col) leads to a dead end
    return False

def print_solution(board):
    n = len(board)
    for row in range(n):
        for col in range(n):
            if board[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

def eight_queens():
    n = 8  # Size of the chessboard
    board = [-1] * n  # Initialize the board
    if solve_queens(board, 0):
        print("Solution found:")
        print_solution(board)
    else:
        print("No solution exists.")

# Run the program
eight_queens()
