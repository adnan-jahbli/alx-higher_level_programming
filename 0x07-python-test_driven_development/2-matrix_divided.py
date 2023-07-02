#!/usr/bin/python3
"""
    A function that devides all the elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given divisor.

    Args:
        matrix: A matrix (list of lists) of int and float numbers
        div (int or float): The divisor.

    Returns:
        list[list[float]]: A new matrix where each element
        is the result of dividing the corresponding element
        of the original matrix by the divisor, rounded to 2 decimal places.

    Raises:
        TypeError: If the matrix is not a valid matrix
        (a list of lists of integers or floats),
        or if each row of the matrix does not have the same size.
        If the divisor is not a number (integer or float).
        ZeroDivisionError: If the divisor is equal to zero.
    """
    msg1 = "matrix must be a matrix (list of lists) of integers/floats"
    msg2 = "Each row of the matrix must have the same size"

    # checking if matrix is a list of lists
    if not matrix or type(matrix) != list:
        raise TypeError(msg1)
    for row in matrix:
        if not row or type(row) != list:
            raise TypeError(msg1)
        if any(type(num) not in [int, float] for num in row):
            raise TypeError(msg1)

    # Checking matrix row sizes
    row_size = len(matrix[0])
    if any(len(row) != row_size for row in matrix):
        raise TypeError(msg2)

    # checking if div is not zero or not a number
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform division on the matrix elements
    new_matrix = []
    for row in matrix:
        new_row = []
        for num in row:
            new_row.append(round(num / div, 2))
        new_matrix.append(new_row)

    return new_matrix
