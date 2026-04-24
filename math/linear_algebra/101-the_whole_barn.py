#!/usr/bin/env python3
"""The Whole Barn"""


def add_matrices(mat1, mat2):
    """Function for The Whole Barn"""
    # Initialize result matrix with zeros
    if isinstance(mat1, list):
        return [add_matrices(i, j) for i, j in zip(mat1, mat2)]
    return mat1+mat2
