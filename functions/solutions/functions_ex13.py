#!/usr/bin/env python3
""" A Solution For functions_ex13
    While the index method of a list can be used to find either the first
    occurrence of an item or the first occurrence of it within a range of
    the list, it does not allow you to find, say the second or third
    occurrence by passing in a number as to the one you are looking for.
    • Write a function that takes 2 parameters; one being the list to search,
      and the other being an  int representing which one you are looking for
      such as the fist, second, third occurrence.
    • The index method raises a ValueError exception if the value being
      searched for does not exit in the list.
    • It is perfectly fine for your function to behave in the same manner.
"""


def get_index(vals, item, occurrence):
    start_at = 0
    for x in range(occurrence):
        found_at = vals.index(item, start_at)
        start_at = found_at + 1
    return found_at


values = [99, 100, 88, 3, 100, 100, 42, 100, 88, 99, 100]
find_me = 100

for offset in range(1, 8):
    print(f"Occurrence {offset} of {find_me} is at",
          get_index(values, find_me, offset))
