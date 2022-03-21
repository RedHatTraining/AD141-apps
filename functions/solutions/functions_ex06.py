#!/usr/bin/env python3
""" A Solution For functions_ex06
    Write and test a function that receives a list as its only parameter and
    returns a new list of the positive elements only.
"""


def positive(alist):
    result = []
    for element in alist:
        if element > 0:
            result.append(element)
    return result


data = [5, -10, 10, -20, 30]
results = positive(data)
print(results)
