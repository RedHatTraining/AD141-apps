#!/usr/bin/env python3
""" A Solution For regular_expressions_ex01
    Write a program that reads a line at a time and determines whether the
    input consists solely of an integer number that is positive or negative.
    • Specify whether it is positive or negative.
"""

import re

while True:
    line = input("input an integer: ")
    ans = re.search(r"^[+-]?\d+$", line)
    if ans:
        print(line, " is all digits")
        if line[0] == '-':
            print("and is negative")
        else:
            print("and is positive")
    else:
        print(line, "is NOT all digits")
