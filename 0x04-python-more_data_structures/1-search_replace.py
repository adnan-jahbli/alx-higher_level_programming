#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    copied_matrix = matrix.copy()

    for i in range(len(matrix)):
        copied_matrix[i] = [element ** 2 for element in matrix[i]]

    return copied_matrix
