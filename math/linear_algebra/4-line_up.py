#!/usr/bin/env python3
"""This module defines adding of matrises"""


def add_arrays(arr1, arr2):
    """Matrix add"""
    add = [0] * len(arr1)
    for i in range(len(arr1)):
        add[i] = arr1[i] + arr2[i]
    return add
