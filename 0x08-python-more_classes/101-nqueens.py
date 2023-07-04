#!/usr/bin/python3
"""
This module implements a backtracking algorithm
for solving the N-Queen puzzle.

"""
import sys


def isSafe(board, row, col):
    """
    Check if a queen can be placed at the given position
    without attacking other queens.

    Args:
        board: 2D list representing the chessboard configuration
        row: Row index of the position to check
        col: Column index of the position to check

    Returns:
        True if a queen can be placed at the given position
        without attacking other queens, False otherwise.
    """
    # Check if there is a queen in the same row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check if there is a queen in the upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check if there is a queen in the lower left diagonal
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solveNQueens(N):
    """
    Solve the N queens problem and print the solutions.

    Args:
        N: Number of queens and size of the chessboard.
    """
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the chessboard
    board = [[0] * N for _ in range(N)]

    # Start solving the problem from the first column
    solveNQueensUtil(board, 0)


def solveNQueensUtil(board, col):
    """
    Recursive utility function to solve the N queens problem.

    Args:
        board: 2D list representing the chessboard configuration
        col: Current column index to consider placing the queen
    """
    if col >= len(board):
        # All queens have been placed, print the solution
        printSolution(board)
        return

    for i in range(len(board)):
        if isSafe(board, i, col):
            # Place a queen at the current position
            board[i][col] = 1

            # Recur to the next column
            solveNQueensUtil(board, col + 1)

            # Backtrack and remove the queen from the current position
            board[i][col] = 0


def printSolution(board):
    """
    Print the chessboard configuration representing a solution.

    Args:
        board: 2D list representing the chessboard configuration
    """
    for row in board:
        print(" ".join(str(cell) for cell in row))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        # Invalid number of arguments, print usage message and exit
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        # Invalid argument, N must be a number
        print("N must be a number")
        sys.exit(1)

    # Solve the N queens problem
    solveNQueens(N)
