#!/usr/bin/env python3
""" A Solution For functions_ex07
    Write and test a function that takes a variable number of arguments
    as its first parameter and a number as its second parameter.
    • The function should return the count of the values in the tuple
      parameter (the variable number of arguments) that are greater than the
      second parameter (num in the sample below).
    • For example, one such call to a function named positive is shown below.
             res = positive(5, -10, 10, -20, 30, num=0)
    • In this case, the function would return a value of 3.
"""


def positive(*numbers, num=0):
    result = 0
    for element in numbers:
        if element > num:
            result += 1
    return result


limit = 20
res = positive(5, -10, 10, -20, 30, num=limit)
print(f"There is/are {res} value(s) greater than {limit}")
