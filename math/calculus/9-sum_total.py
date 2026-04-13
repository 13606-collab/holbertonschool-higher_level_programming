#!/usr/bin/env python3
"""
sum calculation
"""

def summation_i_squared(n):
    """
    function for sum calculation
    """

    sum = 0
    
    if not n:
        return None

    for i in range(1, n+1):
        sum += i*i

    return sum
