#!/usr/bin/env python3
""" A Solution For functions_ex11
    Write and test a function that takes two lists as parameters
    and returns a list of the elements that are common to both.
"""


def common(c1, c2):
    s1 = set(c1)
    s2 = set(c2)
    s3 = s1 & s2
    return list(s3)


a = [10, 40, 30, 20, 5]
b = [80, 70, 60, 50, 40, 30]
c = common(a, b)
print(c)
