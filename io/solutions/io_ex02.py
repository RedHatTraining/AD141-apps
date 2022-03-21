#!/usr/bin/env python3
""" A Solution For functions_ex02
    Revise Exercise 1 so that it accepts as an optional first command line
    argument a -t option.
    • The program should then only print the total number of lines, words,
      and characters in all the files combined.
"""

from sys import argv
fmt = "{:20} {:^5} {:^5} {:^5}"
if len(argv) == 1:
    print("need at least one file argument")
    exit(1)

total = False
argv.pop(0)
if argv[0].startswith("-t"):
    total = True
    argv.pop(0)

tlines = twords = tchars = 0
print(fmt.format("FILE NAME", "LINES", "WORDS", "CHARS"))

for filename in argv:
    f = open(filename, "r")
    lines = words = chars = 0
    for line in f:
        lines += 1
        chars += len(line)
        data = line.split(None)
        words += len(data)
    f.close()
    print(fmt.format(filename, lines, words, chars))
    twords = twords + words
    tchars = tchars + chars
    tlines = tlines + lines

if total:
    print("=" * 30)
    print(fmt.format("TOTALS", tlines, twords, tchars))
