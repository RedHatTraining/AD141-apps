#!/usr/bin/env python3
""" A Solution For functions_ex01
    Write a program that counts the number of lines, words, and characters in
    each file named on the command line.
"""

from sys import argv
fmt = "{:20} {:^5} {:^5} {:^5}"
print(fmt.format("FILE NAME", "LINES", "WORDS", "CHARS"))

for filename in argv[1:]:
    f = open(filename, "r")
    lines = words = chars = 0
    for line in f:
        lines += 1
        chars += len(line)
        data = line.split(None)
        words += len(data)
    f.close()
    print(fmt.format(filename, lines, words, chars))
