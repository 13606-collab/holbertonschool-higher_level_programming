#!/usr/bin/env python3
"""This module defines Concatenates of 2 matrises"""


def cat_matrices2D(mat1, mat2, axis=0):
    """Concatenates of 2 matrices"""
    if axis == 0:
        for row in mat1:
            mat1_columns = len(row)
        for row in mat2:
            mat2_columns = len(row)
        if mat1_columns != mat2_columns:
            return None
        cat_matrix = []
        for x, row in enumerate(mat1):
            cat_matrix.append([])
            for i in row:
                cat_matrix[x].append(i)
        x += 1
        for y, row in enumerate(mat2):
            cat_matrix.append([])
            for i in row:
                cat_matrix[x + y].append(i)
        return cat_matrix
    if axis == 1:
        if len(mat1) != len(mat2):
            return None
        cat_matrix = []
        for z, row in enumerate(mat1):
            cat_matrix.append([])
            for i in mat1[z]:
                cat_matrix[z].append(i)
            for i in mat2[z]:
                cat_matrix[z].append(i)
        return cat_matrix
    return None
