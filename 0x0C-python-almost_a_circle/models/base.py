#!/usr/bin/python3
"""
models/base.py
"""


class Base:
    __no_objects = 0
    def __init__(self, id=None):
        """
        initializing an instance
        """
        if id != None:
            self.id = id
        else:
            Base.__no_objects += 1
            self.id = Base.__no_objects
