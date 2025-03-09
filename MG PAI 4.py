def display_solution(board):
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))
    print("\n")

def can_place_queen(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i][col]:
            return False
    
    # Check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1
    
    # Check upper-right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j]:
            return False
        i -= 1
        j += 1
    
    return True

def find_n_queens_solutions(board, row, n, results):
    if row == n:
        results.append([row[:] for row in board])
        display_solution(board)
        return
    
    for col in range(n):
        if can_place_queen(board, row, col, n):
            board[row][col] = 1
            find_n_queens_solutions(board, row + 1, n, results)
            board[row][col] = 0  # Backtrack

def solve_n_queens_problem(n):
    board = [[0] * n for _ in range(n)]  # Initialize the board
    results = []
    find_n_queens_solutions(board, 0, n, results)
    return results

# Solve the N-Queens problem for a 8x8 board
n = 8
solve_n_queens_problem(n)
