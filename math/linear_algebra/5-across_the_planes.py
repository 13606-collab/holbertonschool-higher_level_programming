#!/usr/bin/env python3
"""This module defines adding of 2D matrises"""


def add_matrices2D(mat1, mat2):
    """2D Matrix add"""
    if not len(mat1) == len(mat2) or not len(mat1[0]) == len(mat2[0]):
        return None
    row = len(mat1)
    column = len(mat1[0])
    add_mat = [[0] * column for _ in range(row)]
    for i in range(row):
        for j in range(column):
            add_mat[i][j] = mat1[i][j] + mat2[i][j]
    return add_mat
