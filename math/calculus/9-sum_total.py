#!/usr/bin/env python3
"""
sum calculation
"""

def summation_i_squared(n):
    """
    function for sum calculation
    """    
    if not isinstance(n, int) or n < 0:
        return None

    sum = (n*(n+1)*(2*n+1))//6

    return sum
