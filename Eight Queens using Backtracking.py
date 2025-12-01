# Q5: 8‑Queens problem using backtracking

def is_safe(board, row, col, n):
    # check column
    for i in range(row):
        if board[i] == col:
            return False
    # check diagonals
    for i in range(row):
        if abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_n_queens(n):
    board = [-1] * n
    solutions = []

    def backtrack(row):
        if row == n:
            solutions.append(board.copy())
            return
        for col in range(n):
            if is_safe(board, row, col, n):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    backtrack(0)
    print("Number of solutions:", len(solutions))
    for sol in solutions:
        for r in range(n):
            line = ""
            for c in range(n):
                line += "Q " if sol[r] == c else ". "
            print(line)
        print()

if __name__ == "__main__":
    solve_n_queens(8)