#!/usr/bin/env python3
""" A Solution For language_ex02

    Write a program that prompts for a lucky number.
    • The program should print out a message if the number entered
      is not an integer.

    Rewrite the above exercise such that additionally it prints
    out how many digits are in the number if it is an integer.
"""

text = input("Please enter a lucky number: ")
if not text.isnumeric():
    print("The value you entered is not an integer")
else:
    print("Your lucky number", text, "has", len(text), "digit(s)")
