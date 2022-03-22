#!/usr/bin/env python3
""" A Solution For functions_ex08
    Write a function that returns a nested function.
    • When the nested function is executed it should return the sum of two
      integers.
    • The two parameters should be passed to the outer function and used by
      the inner function.
"""


def deliver():
    def addthem(a, b):
        return a + b
    return addthem


f = deliver()
print(f(3, 4))
print(f(10, 20))
