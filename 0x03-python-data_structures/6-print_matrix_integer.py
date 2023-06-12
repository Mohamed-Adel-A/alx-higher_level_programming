#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for r in matrix:
        for e in r:
            if(e == r[-1]):
                print("{:d}".format(e), end="")
            else:
                print("{:d}".format(e), end=" ")
    print()
