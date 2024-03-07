#!/usr/bin/python3
"""
Pascal's triangle
"""


def pascal_triangle(n: int) -> list:
    """
    returns a list of lists
    """
    result = [[1]]

    for i in range(n - 1):
        placeholder_variable = [0] + result[-1] + [0]
        row = []
        for j in range(len(result[-1]) + 1):
            row.append(placeholder_variable[j] + placeholder_variable[j + 1])
        result.append(row)

    return result
