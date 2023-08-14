#!/usr/bin/python3
"""add module"""


def add_integer(a, b=98):
    """Add two number together"""
    if (type(a) is not int) and (type(a) is not float):
        raise TypeError("a must be an integer")
        return
    if (type(b) is not int) and (type(b) is not float):
        raise TypeError("b must be an integer")
        return
    return (int(a) + int(b))
