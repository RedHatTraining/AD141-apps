#!/usr/bin/env python3
""" A Solution For collections_ex03

    Write a program that creates a loop asking the user to input a number.
    • Repeat this process until the user enters the value `end`.


    • Enter each number into a set.
    • Before you enter the number, verify if the number is
      already in the set.
    • If the number is already in the set, then update a counter
      that tracks how many entries are not added to the set.
    • Just before the program ends, print the following:
    • The contents of the set on one line
    • The number of elements that were NOT added to the set on the
      second line.
"""
count = 0
numbers = set()
prompt = "Enter a number (or the word 'end' to quit) "
while True:
    data = input(prompt)
    if data == "end":
        break
    # Remainder of while loop goes here
    if data not in numbers:
        numbers.add(data)
    else:
        count += 1

print("The set is:", numbers)
print(count, "values were not unique.")
