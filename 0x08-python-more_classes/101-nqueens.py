#!/usr/bin/python3
"""A program that solves the N queens problem."""
import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    SIZE = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if SIZE < 4:
    print("N must be at least 4")
    sys.exit(1)

def solve_n_queens(N: int):
    """Computes all possible solutions to the problem for a given N.

    Args:
        N (int): Dimension of the chessboard / number of queens.
    """
    def is_safe(board, row, col):
        # Check if it is safe to place a queen at the given position
        for i in range(row):
            if board[i] == col or \
                    board[i] - i == col - row or \
                    board[i] + i == col + row:
                return False
        return True

    def solve(board, row):
        if row == N:
            # All queens have been placed, add the solution to the list
            solutions.append([[i, board[i]] for i in range(N)])
        else:
            for col in range(N):
                if is_safe(board, row, col):
                    board[row] = col
                    solve(board, row + 1)

    solutions = []  # Store the solutions
    board = [-1] * N
    solve(board, 0)

    # Print the solutions in the desired format
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    solve_n_queens(SIZE)

