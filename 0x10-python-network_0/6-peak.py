#!/usr/bin/python3
"""
finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    a function that finds a peak in a list of unsorted integers.
    """
    peek = None
    if not list_of_integers:
        return peek
    if len(list_of_integers) == 0:
        return peek
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    if len(list_of_integers) == 2:
        return max(list_of_integers)
