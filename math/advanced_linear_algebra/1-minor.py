#!/usr/bin/env python3


"""This script calculates the minor of a matrix,
which is the determinant of the submatrix formed
by removing a specific row and column.
It also provides a function to compute 
the full matrix of minors for a given square matrix.
The determinant is calculated recursively
using cofactor expansion.
"""


def validate_matrix(matrix):
    if not type(matrix) is list or not all((type(row) is list) for row in matrix):
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
    if n == 0:
        return 1  # The determinant of an empty matrix is defined as 1
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


if __name__ == '__main__':
    minor = __import__('1-minor').minor

    mat1 = [[5]]
    mat2 = [[1, 2], [3, 4]]
    mat3 = [[1, 1], [1, 1]]
    mat4 = [[5, 7, 9], [3, 1, 8], [6, 2, 4]]
    mat5 = []
    mat6 = [[1, 2, 3], [4, 5, 6]]

    print(minor(mat1))
    print(minor(mat2))
    print(minor(mat3))
    print(minor(mat4))
    try:
        minor(mat5)
    except Exception as e:
        print(e)
    try:
        minor(mat6)
    except Exception as e:
        print(e)