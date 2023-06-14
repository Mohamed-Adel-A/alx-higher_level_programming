#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = [replace if e == search else e for e in my_list]
    return (new_list)
