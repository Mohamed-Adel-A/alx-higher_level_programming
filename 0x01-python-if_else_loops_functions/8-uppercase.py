#!/usr/bin/python3
def uppercase(str):
    i = 0
    for c in str:
        if (ord(c) >= 97 and ord(c) <= 122):
            c = ord(str[i]) - 32
        else:
            c = ord(str[i])
        print("{:c}".format(c), end="")
    print("")
