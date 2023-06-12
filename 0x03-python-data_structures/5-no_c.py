#!/usr/bin/python3
def no_c(my_string):
    for c in my_string:
        if (c == 'C' or c == 'c'):
            c = None
        return (my_string)
