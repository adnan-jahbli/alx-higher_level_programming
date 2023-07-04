#!/usr/bin/python3
"""
This module implements a backtracking algorithm
for solving the N-Queen puzzle.
"""


def is_safe(queens_positions, current_queen):
    """Check if the queens can attack each other.

    Args:
        queens_positions (list): List of queens' positions.
        current_queen (int): Index of the current queen.

    Returns:
        bool: True if the queens can't attack each other, False otherwise.
    """
    for i in range(current_queen):
        if queens_positions[i] == queens_positions[current_queen]:
            return False
        if abs(queens_positions[i] - queens_positions[current_queen]) \
                == abs(i - current_queen):
            return False
    return True


def print_queens_positions(queens_positions, size):
    """Print the positions of the queens on the chessboard.

    Args:
        queens_positions (list): List of queens' positions.
        size (int): Size of the chessboard.
    """
    positions = []
    for i in range(size):
        positions.append([i, queens_positions[i]])
    print(positions)


def solve_n_queens(size):
    """Solve the N-Queen puzzle using backtracking.

    Args:
        size (int): Size of the chessboard.
    """
    queens_positions = [-1] * size

    def queen_backtracking(current_queen):
        if current_queen == size:
            print_queens_positions(queens_positions, size)
            return

        queens_positions[current_queen] = -1

        while queens_positions[current_queen] < size - 1:
            queens_positions[current_queen] += 1
            if is_safe(queens_positions, current_queen):
                queen_backtracking(current_queen + 1)

    queen_backtracking(0)


if __name__ == '__main__':
    import sys

    if len(sys.argv) == 1 or len(sys.argv) > 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        size = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if size < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_n_queens(size)
