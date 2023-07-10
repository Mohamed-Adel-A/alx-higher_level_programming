#!/usr/bin/python3
""" 13. Can I? """


def add_attribute(obj, attribute, value):
    """
    a function that adds a new attribute to an object if it’s possible
    """
    if not hasattr(o, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
