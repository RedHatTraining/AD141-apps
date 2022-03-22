#!/usr/bin/env python3
""" A Solution For modules_ex04
    Write a program that sums the command line arguments.
    • The program should print both the sum of the arguments
      and the average value.
"""
from sys import argv

total = 0
for item in argv[1:]:
    total += float(item)

print("Total:", total)
print("Average:", total / (len(argv) - 1))
