#!/usr/bin/env python3
"""
integral of poly
"""


def poly_integral(poly, C=0):
    """
    function for integral poly
    """
    if not isinstance(poly, list) or isinstance(C, int):
        return None
    if not poly:
        return [C]
    new_poly = [C]
    for i in range(1, len(poly)):
        new_poly.append(poly[i]/(i+1))
    if new_poly == []:
        return [0]
    return new_poly
