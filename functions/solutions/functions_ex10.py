#!/usr/bin/env python3
""" A Solution For functions_ex10
    Re-write your solution to either Exercise 8 or 9 so that it uses a
    lambda expression as the nested function.
"""


def deliver():
    return lambda x, y: x + y


f = deliver()
print(f(3, 4))
print(f(10, 20))
