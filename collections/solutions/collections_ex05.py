#!/usr/bin/env python3
""" A Solution For collections_ex05

    Use a dictionary to create a mapping from the digits 0-9
    to the words 'zero', 'one,' 'two,' etc.
    • Next, ask the user to input a number.
    • If the user enters 1437, then the program should print
      "one four three seven."
"""
the_map = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
           5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}

number = input("Enter a number: ")

for digit in number:
    print(the_map[int(digit)], end=" ")

print()

# Alternate Solution
the_map = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
           '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}

number = input("Enter a number: ")

for digit in number:
    print(the_map[digit], end=" ")

print()
