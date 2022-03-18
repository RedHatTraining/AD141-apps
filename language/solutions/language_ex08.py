#!/usr/bin/env python3
""" A Solution For language_ex08

    Write a program that prompts twice for an integer.
    • The program should output the sum of the integers within
      the range of those two numbers inclusively.
    • For example, if the user inputs the numbers 10 and 15
      then the sum would be 75.
          10 + 11 + 12 + 13 + 14 + 15 = 75

    Rewrite language_ex04 such that the program takes into account
    the case where the first number entered is bigger than the first.
    • For example, if the user inputs the numbers 10 and 15
      then the sum would be 75.
          10 + 11 + 12 + 13 + 14 + 15 = 75
    • While if the user inputs the numbers 15 and 10, then the sum
      would be still be 75.

"""
prompt = "Enter {} integer: "
first = int(input(prompt.format("an")))
second = int(input(prompt.format("a second")))

if first > second:
    first, second = second, first  # Swap the values inn a Pythonic way


counter = first
total = 0
while(counter <= second):
    total += counter
    counter += 1

print("Total = ", total)

# Alternative way to calculate the sum
total = 0
for value in range(first, second + 1):
    total += value

print("Total = ", total)
