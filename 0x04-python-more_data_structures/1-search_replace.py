#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if (my_list and search and replace):
        #new_list = [replace if e == search else e for e in my_list]
        new_list = []
        for e in my_list:
            if e == search:
                new_list.append(replace)
            else:
                new_list.append(e)
        return (new_list)
