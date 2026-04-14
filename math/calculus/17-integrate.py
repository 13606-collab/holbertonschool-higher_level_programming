#!/usr/bin/env python3
"""
integral of poly
"""


def poly_integral(poly, C=0):
    """
    function for integral poly
    """
    if not isinstance(poly, list) or not isinstance(C, int):
        return None
    if not poly:
        return [C]
    new_poly = [C]
    for i in range(1, len(poly)):
        x = poly[i]/(i+1)
        if x.is_integer():
            new_poly.append(int(x))
        else:
            new_poly.append(x)
    if new_poly == []:
        return [0]
    return new_poly
