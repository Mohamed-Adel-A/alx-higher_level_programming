#!/usr/bin/python3
def max_integer(my_list=[]):
    if (my_list):
        max = my_list[0]
        for e in my_list:
            if e > max:
                max = e
        return (max)
    else:
        return (None)
