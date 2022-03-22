#!/usr/bin/env python3
""" A Solution For basics_ex01
    Write a program that prompts to enter a string of text.
    The program should print the original text followed on a
    second line in the output by the number of characters entered.
"""

text = input("Please enter some text: ")
print("The text you typed:", text)
print("Has", len(text), "characters in it.")
