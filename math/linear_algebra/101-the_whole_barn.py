#!/usr/bin/env python3
"""The Whole Barn"""


def add_matrices(mat1, mat2):
    """Function for The Whole Barn"""
    # Initialize result matrix with zeros    
    if len(mat1) != len(mat2):
        return None

    result = []
    for i in range(len(mat1)):
       
        row1 = mat1[i]
        row2 = mat2[i]
        if len(row1) != len(row2):
            return None
        row = []
        for j in range(len(row1)):
            row.append(row1[j] + row2[j])
        result.append(row)
        
    return result
