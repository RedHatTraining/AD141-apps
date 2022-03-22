#!/usr/bin/env python3
""" A Solution For functions_ex12
    Write and test a function that takes a number and a dictionary
    and adds the number to all values in the dictionary.
    • You can assume that all the values in the dictionary are numbers.
"""


def addn(theMap, number):
    for i in theMap.keys():
        theMap[i] = theMap[i] + number


h = {'a': 10, 'b': 20, 'c': 30}
print(h)
addn(h, 10)
print(h)
