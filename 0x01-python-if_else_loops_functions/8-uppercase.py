#!/usr/bin/python3
def uppercase(str):
    i = 0
    while str[i] != '\0':
        if (ord(str) >= 97 and ord(str) <= 122):
            c = ord(str[i]) - 32
        else:
            c = ord(str[i])
        
        print("{:c}".format(c))
