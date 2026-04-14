#!/usr/bin/env python3
"""
derivative of poly
"""


def poly_derivative(poly):
    """
    function for poly
    """
    if not isinstance(poly, list) or len(poly) == 0:
        return None
    new_poly = []
    for i in range(1, len(poly)):
        new_poly.append(i*poly[i])
    if new_poly == []:
        return [0]
    return new_poly
