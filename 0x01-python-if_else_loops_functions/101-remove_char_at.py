#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    for c in str:
        if (i == n):
            continue
        else:
            new_str[i] = c
            i++
        return (new_str)
