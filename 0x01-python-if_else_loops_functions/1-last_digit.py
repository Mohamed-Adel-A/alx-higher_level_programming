#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number = -98
Last_digit = number % 10
print(Last_digit)
if Last_digit > 5:
    print(f"Last digit of {number} is {Last_digit} and is greater than 5")
elif Last_digit == 0:
    print(f"Last digit of {number} is {Last_digit} and is 0")
else:
    print(f"Last digit of {number} is {Last_digit} and ", end="")
    print("is less than 6 and not 0")
