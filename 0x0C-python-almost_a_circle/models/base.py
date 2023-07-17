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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
            list_objs: is a list of instances who inherits of Base
        """
        file_name = cls.__name__ + ".json"
        with open(file_name, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dictionaries = [obj.to_dictionary() for obj in list_objs]
                f.write(Base.to_json_string(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
        json_string: is a string representing a list of dictionaries
        """
        if (json_string is None or json_string == "[]"):
            return []
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set:
        """
        if (cls.__name__ == "Rectangle"):
            newobj = cls(1, 1)
        elif (cls.__name__ == "Square"):
            newobj = cls(1)
        newobj.update(**dictionary)
        return (newobj)
        
