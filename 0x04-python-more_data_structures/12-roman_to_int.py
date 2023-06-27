#!/usr/bin/python3
def roman_to_int(roman_string):
    if (roman_string is None or type(roman_string) != str):
        return (0)
    letters_values = {"I": 1, "V": 5, "X": 10, "L": 50,
                      "c": 100, "D": 500, "M": 1000}
    sum = 0
    bigger = 1
    prev = 3000
    for c in roman_string:
        if letters_values[c] > prev:
            sum -= (prev * 2)
        sum += letters_values[c]
        prev = letters_values[c]
    return (sum)
