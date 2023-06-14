#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for k in (list(a_dictionary.keys())).sort():
        print(f"{k}: {a_dictionary[k]}")
