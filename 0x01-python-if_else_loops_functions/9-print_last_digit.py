#!/usr/bin/python3
def print_last_digit(number):
    Last_digit = abs(number) % 10
    if (number < 0):
        Last_digit *= -1
    print(f"{Last_digit}", end="")
    return (Last_digit)
