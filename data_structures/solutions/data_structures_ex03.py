#!/usr/bin/env python3
""" A Solution For data_structures_ex03
    Write a dictionary comprehension that generates a dictionary of numbers
    and their factorials in the range (1,10).
    • Using that dictionary, multiply 6 factorial times 5 factorial.
"""


def fact(p):
    ans = p
    while (p > 2):
        p -= 1
        ans *= p
    return ans


# dict of fact pairs
dictionary = dict([(x, fact(x)) for x in range(1, 11)])
print(dictionary)
print(dictionary[5] * dictionary[6])
