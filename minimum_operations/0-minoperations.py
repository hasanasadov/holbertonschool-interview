#!/usr/bin/python3
"""function"""


def minOperations(n):
    """Args:
            n: repetitions of H

        Returns:
            number of operations (Copy & Paste) to reach n Hs
    """
    operations = 0
    summation = 1
    carrier = 0

    while summation < n:
        if n % summation == 0:
            carrier = summation
            summation *= 2
            operations += 1
        else:summation += carrier
        operations += 1  # Always paste

    return operations
