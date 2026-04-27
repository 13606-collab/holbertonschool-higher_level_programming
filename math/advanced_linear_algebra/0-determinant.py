#!/usr/bin/env python3
"""Moduole"


def determinant(matrix):
    """
    Calculate the determinant of a square matrix.

    Args:
        matrix (list of lists): The matrix to compute determinant for.

    Returns:
        int or float: The determinant value.

    Raises:
        TypeError: If matrix is not a list of lists.
        ValueError: If matrix is not square.
    """

    # Check type
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    # Handle 0x0 case
    if matrix == [[]]:
        return 1

    n = len(matrix)
    # Check square
    if any(len(row) != n for row in matrix):
        raise ValueError("matrix must be a square matrix")

    # Base cases
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

    # Recursive expansion (Laplace expansion along first row)
    det = 0
    for col in range(n):
        # Build minor
        minor = [row[:col] + row[col+1:] for row in matrix[1:]]
        det += ((-1)**col) * matrix[0][col] * determinant(minor)

    return det
