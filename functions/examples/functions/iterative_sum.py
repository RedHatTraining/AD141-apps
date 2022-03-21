#!/usr/bin/env python3
def iterative_sum_to(n):
    total = 0
    for i in range(n, 0, -1):
        total += i
    return total


limit = 6
print("Sum from 1 to", limit, "is:", iterative_sum_to(limit))
