#!/usr/bin/python3
"""
models/base.py
Base class
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """
        if (list_dictionaries is None):
            return ("[]")
        return (json.dumps(list_dictionaries))
