#!/usr/bin/env python3
def sum_to(n):
    if not n:     # This is the termination condition
        return n

    return n + sum_to(n-1)  # This is where the recursion is


limit = 6
print("Sum from 1 to", limit, "is:", sum_to(limit))
