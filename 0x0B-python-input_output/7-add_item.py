#!/usr/bin/python3
"""
a script that adds all arguments to a Python list,
and then save them to a file
"""
import json
import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

if __name__ == "__main__":
    try:
        l = load_from_json_file("add_item.json")
    except FileNotFoundError:
        l = []

    l += argv[1:]
    save_to_json_file(l, "add_item.json")
        
