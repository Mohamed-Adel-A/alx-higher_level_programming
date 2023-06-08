#!/usr/bin/python3
if __name__ = "__main__":
    from sys import argv
    args_len = len(argv)
    sum = 0
    if args_len > 1:
        for i in ragne(1, args_len):
            sum = sum + int(argv[i])
    print("{:d}".format(sum))
