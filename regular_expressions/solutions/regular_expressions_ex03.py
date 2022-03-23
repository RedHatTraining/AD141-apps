#!/usr/bin/env python3
""" A Solution For regular_expressions_ex03
    Write a program that reads lines from the user one at a time to see if
    they are formatted according to the following criteria.
    • Correctly formatted lines should consist of a four character identifier,
      any number of spaces or tabs, and a description.
    • The four character identifier should consist of two digits followed by
      two uppercase characters.
    • For each correctly formatted line, print the two digits, the two
      characters, and the descriptions.
      ▶ Print all of these pieces of information on separate lines.
"""


import re

while True:
    line = input("input a line: NNAA ... DESC: ")
    ans = re.search(r"^(\d\d)([A-Z][A-Z])\s+(.*)$", line)
    if ans:
        print("NUMBER IS", ans.group(1))
        print("ALPHA IS", ans.group(2))
        print("DESC IS", ans.group(3))
    else:
        print(line, "DOES NOT MATCH NNAA ... DESC")
