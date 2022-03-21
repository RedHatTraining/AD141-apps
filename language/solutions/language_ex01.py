#!/usr/bin/env python3
""" A Solution For language_ex01

    Write a program that prompts for a lucky number.
    • The program should print out a message if the number entered
      is not an integer.
"""
text = input("Please enter a lucky number: ")
if not text.isnumeric():
    print("The value you entered is not an integer")
