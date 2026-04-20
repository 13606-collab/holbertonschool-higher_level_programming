#!/usr/bin/env python3
"""This module dwefine dimension of matrix"""


def matrix_shape(matrix):
    """ dimension of matrix"""
    matrix_shape = []
    while (type(matrix) is list):
        matrix_shape.append(len(matrix))
        matrix = matrix[0]
    return matrix_shape
