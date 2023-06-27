#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        ret = fct(*args)
        return (ret)
    except Exception as exp:
        print("Exception: {}".format(exp), file=sys.stderr)
        return None
