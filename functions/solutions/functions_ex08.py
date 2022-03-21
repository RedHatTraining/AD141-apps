#!/usr/bin/env python3
"""Outer function returns a nested function"""
def outer(a, b):

    def inner():
        return a + b

    return inner  # a reference to inner function


result = outer(5, 10)
print(type(result))
print("Function returns:",result())  # invoke the returned function
