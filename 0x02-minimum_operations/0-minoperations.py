#!/usr/bin/python3
""" This script calculates the minimum number of operations to achieve
    a given number of characters using only “Copy All” and “Paste”
    operations
"""


def minOperations(n):
    """ calculates the minimum number of operations"""
    if n < 2:
        return 0
    for f in range(2, int(n ** 0.5) + 1):
        if n % f == 0:
            return f + minOperations(n // f)
    return n
