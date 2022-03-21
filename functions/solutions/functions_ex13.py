#!/usr/bin/env python3
"""Return the index of the nth occurance of an item in a list"""
def nth_index(a_list, item, n):
    current = 1
    index = a_list.index(item)
    next = index + 1
    if n == current:
        return index

    while current < n:
        current += 1
        index = a_list[next:].index(item)
        next += (index + 1)
    
    return next - 1 

test = "1 2 3 4 1 2 3 4 5 1 3 1 4 5 2 3 4 5 5".split()
print("The first index of 1 in the list",test,"is",nth_index(test, "1", 1))
print("The second index of 1 is",nth_index(test, "1", 2))
print("The third index of 1 is",nth_index(test, "1", 3))
print("The forth index of 1 is",nth_index(test, "1", 4))
