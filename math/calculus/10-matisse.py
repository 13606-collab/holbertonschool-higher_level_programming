#!/usr/bin/env python3
"""
derivative of poly
"""


def poly_derivative(poly):
    """
    function for poly
    """
    if len(poly) < 2:
        return None
    new_poly = []
    for i in range(1, len(poly)):
        new_poly.append(i*poly[i])
    return new_poly
