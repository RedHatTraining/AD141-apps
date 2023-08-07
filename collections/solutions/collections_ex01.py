#!/usr/bin/env python3
""" A Solution For collections_ex01
    Given the following two lists:

    first = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    second = ["day", "day", "sday", "nesday", "rsday", "day", "urday"]

    • Concatenate the two lists by index into a new list that when printed
      looks as follows:
['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
"""


first = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
second = ["day", "day", "sday", "nesday", "rsday", "day", "urday"]
days = []
for index, day in enumerate(first):
    days.append(f'{day}{second[index]}')

print(days)
