# N-Queens using Backtracking
def print_board(board, N):
    for i in range(N):
        row = ""
        for j in range(N):
            row += "Q " if board[i] == j else ". "
        print(row)
    print()

def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_n_queens(board, row, N):
    if row == N:
        print_board(board, N)
        return True  # to print only one solution; remove this line to print all

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            if solve_n_queens(board, row + 1, N):
                return True
            board[row] = -1  # backtrack
    return False

# --- Main program ---
N = 4
board = [-1] * N
print("Solution for", N, "Queens using Backtracking:")
solve_n_queens(board, 0, N)
