#!/usr/bin/python3
from math import factorial
"""
Pascal's triange
"""


def pascal_triangle(n):
    """
    returns a list of lists
    """
    pass

def factorial(n):
    """
    returns a factorial
    using recusion
    """
    if n == 0:
        return 1
    else:
        return ( n * factorial(n -1))
    
def combination(n, a):
    pass



if __name__ == "__main__":
    print(pascal_triangle(6))