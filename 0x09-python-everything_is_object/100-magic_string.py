#!/usr/bin/python3

def magic_string():
    magic_string.times = getattr(magic_string, 'times', 0)
    return "BestSchool, " * (magic_string.times) + "BestSchool"
