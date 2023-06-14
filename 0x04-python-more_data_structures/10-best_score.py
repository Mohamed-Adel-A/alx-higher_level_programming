#!/usr/bin/python3
def best_score(a_dictionary):
    if (a_dictionary):
        best = 0
        best_key = ""
        for k, v in a_dictionary.items():
            if v > best:
                best = v
                best_key = k
        return (best_key)
    else:
        return (None)
