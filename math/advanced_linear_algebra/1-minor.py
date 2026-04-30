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


def minor_matrix(matrix):
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


# ── Example usage ──────────────────────────────────────────────
if __name__ == "__main__":

    #  Test 0: normal case
    M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print_matrix(M, "Original Matrix")
    print("Minor at (0,0):", get_minor(M, 0, 0))
    print_matrix(minor_matrix(M), "Minor Matrix")

    # Test 1: matrix is not a list of lists
    try:
        get_minor("not a matrix", 0, 0)
    except TypeError as e:
        print(f"\nTypeError: {e}")

    #  Test 2: matrix is empty
    try:
        get_minor([], 0, 0)
    except ValueError as e:
        print(f"ValueError: {e}")

    #  Test 3: matrix is not a square matrix
    try:
        get_minor([[1, 2], [3, 4], [5, 6]], 0, 0)
    except ValueError as e:
        print(f"ValueError: {e}")