#!/usr/bin/env python3
""" A Solution For functions_ex03
    There is a built-in function in Python called sum that will return the
    sum of all of the numbers of an iterable object.
    • Write a similar function, but instead of taking a collection as a
      parameter, the function should take a variable number of arguments
      and return the sum of them.
"""


def get_sum(*args):
    return sum(args)


print(f"sum of 9, 8, 7 is {get_sum(9, 8, 7)}")
print(f"sum of 17, 10, 3, 5, 1, 6 is {get_sum(17, 10, 3, 5, 1, 6)}")
