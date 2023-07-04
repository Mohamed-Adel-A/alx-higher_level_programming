#!/usr/bin/python3
def magic_string():
    magic_string.times = 1 + getattr(magic_string, 'times', 0)
    return ("BestSchool, " * (magic_string.times - 1) + "BestSchool")
