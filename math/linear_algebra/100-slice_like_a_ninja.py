#!/usr/bin/env python3


"""_summary_"""
def np_slice(matrix, axes={}):
    """_summary_

    Args:
        matrix (_type_): _description_
        axes (dict, optional): _description_. Defaults to {}.

    Returns:
        _type_: _description_
    """
    dimensions = len(matrix.shape)
    slices_matrix = dimensions * [slice(None)]
    for axis, value in axes.items():
        slices_matrix[axis] = slice(*value)
    return matrix[tuple(slices_matrix)]