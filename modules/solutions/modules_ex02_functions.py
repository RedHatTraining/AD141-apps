#!/usr/bin/env python3
""" A Solution For modules_ex02 Part 1
    Create a new file and define a function in it with the same
    name (but different behavior) as one of the functions from
    the previous exercise.
"""
import sys

fmt = "Inside of Function: {} of module {}"


def one():
    print(fmt.format(one.__name__, __name__) + ", from path: " + str(sys.path[0]))


def two():
    print(fmt.format(two.__name__, __name__) + ", from path: " + str(sys.path[0]))


