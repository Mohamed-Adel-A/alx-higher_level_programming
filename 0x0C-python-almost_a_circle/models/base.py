#!/usr/bin/python3
"""
models/base.py
Base class
"""
import json
import csv


class Base:
    """
    base class
    """
    __no_objects = 0

    def __init__(self, id=None):
        """
        initializing an instance
        """
        if id is not None:
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

    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances
        """
        file_name = cls.__name__ + ".json"
        try:
            with open(file_name) as f:
                list_dictionaries = Base.from_json_string(f.read())
                return [cls.create(**dict) for dict in list_dictionaries]
        except FileNotFoundError:
            return (list())

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        serializes to CSV file
        """
        file_name = cls.__name__ + ".csv"
        with open(file_name, "w") as f:
            if (list_objs is None):
                f.write("[]")
            else:
                if (cls.__name__ == "Rectangle"):
                    names = ["id", "width", "height", "x", "y"]
                elif (cls.__name__ == "Square"):
                    names = ["id", "size", "x", "y"]
                w = csv.DictWriter(f, fieldnames=names)
                for o in list_objs:
                    w.writerow(o.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        deserializes CSV file
        """
        file_name = cls.__name__ + ".csv"
        try:
            with open(file_name, newline="") as f:
                if (cls.__name__ == "Rectangle"):
                    names = ["id", "width", "height", "x", "y"]
                elif (cls.__name__ == "Square"):
                    names = ["id", "size", "x", "y"]
                reader = csv.DictReader(f, fieldnames=names)
                list_dicts = [dict([key, int(value)]
                              for key, value in obj.items())
                              for obj in reader]
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return (list())
