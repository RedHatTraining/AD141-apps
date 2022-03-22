#!/usr/bin/env python3
""" A Solution For modules_ex01 Part 1
    Define a few functions and place them in a module.
"""

fmt = "Inside of Function: {} of module {}"


def one():
    print(fmt.format(one.__name__, __name__))


def two():
    print(fmt.format(two.__name__, __name__))
