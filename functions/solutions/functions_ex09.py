#!/usr/bin/env python3
"""Outer function returns a nested function that takes paramenters"""
def outer():

    def inner(a, b):
        return a + b

    return inner  # a reference to inner function


result = outer()
print(type(result))
print("Function returns:",result(10, 5))  # invoke the returned function
