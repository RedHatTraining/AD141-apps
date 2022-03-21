#!/usr/bin/env python3
""" A Solution For functions_ex09
    Write a function that returns a nested function.
    • When the nested function is executed it should return the sum of two
      integers.
    • The two parameters should be passed to the outer function and used by
      the inner function.

    Re-write the above solution such that the outer function
    receives no parameters, and the nested function is defined as taking
    the two parameters.
"""


def deliver(a, b):
    def addthem():
        return a + b
    return addthem


f = deliver(10, 20)
print(f())
