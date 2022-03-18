#!/usr/bin/env python3
""" A Solution For language_ex05

    Ask the user to input multiple numbers on one input line.
    • Split the numbers into a list.
    • Write a loop that examines each element of the list and
      displays the ones that are greater than zero.
"""
line = input("Enter some numbers separated by spaces: ")
numbers = line.split()

for number in numbers:
    number = float(number)
    if number > 0:
        print(number, end=" ")
print()
