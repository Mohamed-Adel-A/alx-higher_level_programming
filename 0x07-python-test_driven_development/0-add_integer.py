#!/usr/bin/python3
"""add module"""


def add_integer(a, b=98):
    """Add two number together"""
    if (type(a) is not int) and (type(a) is not float):
        print("a must be an integer")
        return
    if (type(b) is not int) and (type(b) is not float):
        print("b must be an integer")
        return
    return (int(a) + int(b))
