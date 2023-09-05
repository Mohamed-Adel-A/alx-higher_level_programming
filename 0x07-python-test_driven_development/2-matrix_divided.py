#!/usr/bin/python3
"""
a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """a function that divides all elements of a matrix."""

    if (type(matrix) is not list) or (matrix == []):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    for ls in matrix:
        if (type(ls) is not list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if len(ls) != len(matrix[0]):
            raise TypeError(
                "Each row of the matrix must have the same size")
        for e in ls:
            if (type(e) is not int) and (type(e) is not float):
                raise TypeError(
                    "matrix must be a matrix (list of lists)\
                    of integers/floats")

    if (type(div) is not int) and (type(div) is not float):
        raise TypeError("div must be a number")

    if (div == 0):
        raise ZeroDivisionError("division by zero")

    new_matrix = [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
    return (new_matrix)
