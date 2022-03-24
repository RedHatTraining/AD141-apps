#!/usr/bin/env python3
""" A Solution For functions_ex07
    Create two data files, each with a set of names, one per line.
    • Now, write a program that reads both files and lists only those
      names that are in both files.
    • The two file names should be supplied on the command line.
"""

import sys

if len(sys.argv) != 3:
    print("Need two argument files")
    exit(1)

f1 = open(sys.argv[1], "r")
f2 = open(sys.argv[2], "r")

s1 = set()
for line in f1:
    s1.add(line)

s2 = set()
for line in f2:
    s2.add(line)

s3 = s1 & s2
for line in s3:
    print(line, end="")
