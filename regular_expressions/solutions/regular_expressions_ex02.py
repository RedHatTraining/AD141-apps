#!/usr/bin/env python3
""" A Solution For regular_expressions_ex02
    Repeat the previous exercise, but this time use a floating point number.
    • A floating point number should have at least one digit to the left and
      to the right of the decimal point.
    • Specify whether the number is positive or negative.
"""

import re

while True:
    line = input("input an floating point number: ")
    ans = re.search(r"^[+-]?\d+\.\d+$", line)
    if ans:
        print(line, " is a floating point number")
        if line[0] == '-':
            print("and is negative")
        else:
            print("and is positive")
    else:
        print(line, "is NOT a floating point number")
