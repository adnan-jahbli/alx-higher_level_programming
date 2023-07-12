#!/usr/bin/python3
""" This module contains the function passcal_triangle """


def pascal_triangle(n):
    """ This function returns the Pascal's triangle

    Args:
        n: the number of rows

    Returns:
        triangle: a list of lists representing the Pascal's triangle

    """

    triangle = []
    prev_row = []

    for i in range(n):
        row = []
        prev_index_1 = -1
        prev_index_2 = 0
        for j in range(len(prev_row) + 1):
            if prev_index_1 == -1 or prev_index_2 == len(prev_row):
                row += [1]
            else:
                row += [prev_row[prev_index_1] + prev_row[prev_index_2]]
            prev_index_1 += 1
            prev_index_2 += 1
        triangle.append(row)
        prev_row = row[:]

    return triangle
