#!/usr/bin/env python3


"""This script calculates the minor of a matrix,
which is the determinant of the submatrix formed by removing a specific row and column.
It also provides a function to compute the full matrix of minors for a given square matrix.
The determinant is calculated recursively using cofactor expansion.
"""


def validate_matrix(matrix):
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    
    if len(matrix) == 0 or any(len(row) != len(matrix) for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")


def get_minor(matrix, row, col):
    validate_matrix(matrix)
    submatrix = [
        [matrix[i][j] for j in range(len(matrix[i])) if j != col]
        for i in range(len(matrix)) if i != row
    ]
    return determinant(submatrix)


def determinant(matrix):
    n = len(matrix)

    if n == 1:
        return matrix[0][0]

    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for col in range(n):
        sign = (-1) ** col
        det += sign * matrix[0][col] * get_minor(matrix, 0, col)

    return det


def minor(matrix):
    validate_matrix(matrix)
    n = len(matrix)
    return [
        [get_minor(matrix, i, j) for j in range(n)]
        for i in range(n)
    ]


def print_matrix(matrix, title="Matrix"):
    print(f"\n{title}:")
    for row in matrix:
        print([round(x, 4) for x in row])