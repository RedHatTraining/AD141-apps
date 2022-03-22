#!/usr/bin/env python3
""" A Solution For data_structures_ex01
    Write list comprehensions to produce the following.
    • A list of elements 0,1,2,3,4,…,99
    • A list from the above comprehension of those values that are evenly
      divisible by 5.
"""

lis = [x for x in range(0, 100)]
print(lis)


by5 = [x for x in lis if x % 5 == 0]
print(by5)
