#!/usr/bin/env python3
""" A Solution For basics_ex02
    Write a program that prompts twice for text from the user.
    • The first input should be a first name.
    • The second input should be a last name.
    • The program should print the full name on one line and the person's
      initials on the second line.
"""

first_name = input("Please enter a first name: ")
last_name = input("Please enter a last name: ")
print(first_name, last_name)
print(first_name[0], last_name[0])
