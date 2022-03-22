#!/usr/bin/env python3
tests = {"Sally": (89, 78, 99, 88, 92, 98, 95, 78, 88),
         "Doug": (68, 87, 72, 60, 80, 65),
         "Kesha": (98, 87, 99, 78, 99, 80, 98, 50),
         "John": (89, 78, 99, 88, 92, 99, 95, 88, 95, 99)}


def averages(*grades):
    qty = len(grades)
    return sum(grades)/qty


a, b, c, d = tests.values()
x = map(averages, a, b, c, d)
print("Averages:", list(x))


# Notice that when an asterisk is used on an iterable
# argument when a function is called, that it unpacks the
# iterable automatically into the arguments passed to the
# function as seen below. This * operator when used in
# this manner is often referred to as the "splat" operator
# in other languages.

x = map(averages, *tests.values())
print("Averages:", list(x))
