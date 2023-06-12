#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if (matrix):
        for r in matrix:
            for e in r:
                print("{:d}".format(e), end="")
                if(e != r[-1]):
                    print(" ")
        print()
