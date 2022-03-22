#!/usr/bin/env python3
""" A Solution For modules_ex03
    Write a program that sorts its command line arguments.
"""
from sys import argv

argv.pop(0)
argv.sort()
for arg in argv:
    print(arg)
