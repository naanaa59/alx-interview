#!/usr/bin/python3
""" This script define a function named pascal_triangle that
build up and return n rows of a pascal's triangle represented by
list of lists"""


def pascal_triangle(n):
    """ returns a list of n lists where each list is a row"""
    if n <= 0:
        return []

    triangle = [[1]]

    for row in range(1, n):
        new_row = [1]
        for col in range(1, row):
            new_row.append(triangle[row - 1][col - 1] + triangle[row - 1][col])
        new_row.append(1)
        triangle.append(new_row)
    return triangle
