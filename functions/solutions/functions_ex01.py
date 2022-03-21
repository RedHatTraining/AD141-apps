#!/usr/bin/env python3
""" A Solution For functions_ex01
    Write and test a function that is designed to validate input.
    • The function should prompt the user for a positive integer.
    • It should validate the information entered by the user is indeed a
      positive integer.
    • If number entered is valid, the function should return the number.
    • If the number entered is invalid, the function should return a zero
     (0) instead.
    • The application, not the function, should indicate with a message in
      the output each time an invalid entry is given.
"""


def validate_input():
    value = input("Enter a positive integer: ")
    if value.isnumeric():
        return int(value)
    else:
        return 0


result = validate_input()
if not result:
    print("Invalid entry given.")
