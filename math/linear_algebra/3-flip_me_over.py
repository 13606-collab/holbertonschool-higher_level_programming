#!/usr/bin/env python3
"""This module defines transpose of matrix"""


def matrix_transpose(matrix):
    """Matrix transpose"""
    row = len(matrix)
    column = len(matrix[0])

    transpose = [[0] * row for _ in range(column)]
    for i in range(row):
        for j in range(column):
            transpose[j][i] = matrix[i][j]

    return transpose
