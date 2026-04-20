#!/usr/bin/env python3
"""This module is for matrix multiplicaton"""


def mat_mul(mat1, mat2):
    """function for matrix multiplivaton"""
    if not len(mat1[0]) == len(mat2):
        return None
    row = len(mat1)
    column = len(mat2[0])
    centre = len(mat1[0])
    new_mat = [[0]*column for _ in range(row)]
    for i in range(row):
        for j in range(column):
            mult = 0
            for l in range(centre):
                mult += mat1[i][l] * mat2[l][j]
            new_mat[i][j] = mult
    return new_mat
