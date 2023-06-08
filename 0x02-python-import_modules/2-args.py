#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    args_len = len(argv)
    if args_len == 1:
        print("0 arguments.")
    elif args_len == 2:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    elif args_len > 2:
        print("{:d} arguments:".format(args_len))
        for i in range(1, args_len):
            print("{:d}: {}".format(args_len, argv[i]))
