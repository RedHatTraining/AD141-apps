#!/usr/bin/env python3
def the_sum(*args):
    total = 0
    print("Parameter type:", type(args), end=" ")
    for elem in args:
        total += elem
    return total


total = the_sum(1, 2, 3, 4, 5)
print("Sum is: ", total)
total = the_sum(5, 2, 7)
print("Sum is: ", total)
