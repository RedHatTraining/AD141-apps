#!/usr/bin/env python3
""" A Solution For functions_ex04
    There is a built-in function in Python called sum that will return the
    sum of all of the numbers of an iterable object.
    • Write a similar function, but instead of taking a collection as a
      parameter, the function should take a variable number of arguments
      and return the sum of them.

    Rewrite the above function  to return a tuple instead of a sum.
    • The tuple should be the sum and the average of all of the
      arguments passed to the function.
"""


def get_sum_avg(*args):
    total = sum(args)
    return(total, total/len(args))


total, avg = get_sum_avg(9, 8, 7)
print(f"sum of 9, 8, 7 is {total}, average is {avg}")
avg, total = get_sum_avg(17, 10, 3, 5, 1, 6)
print(f"sum of 17, 10, 3, 5, 1, 6 is {total}, average is {avg}")
