#!/usr/bin/env python3

""" A Solution For basics_ex04
    Write a program that asks the user to enter a sentence.
    • The program should determine and print the following information:
    • The first character in the string of text and the number of times it
      occurs in the string.
    • The last character in the string of text and the number of times it
      occurs in the string.
"""

data = input("Please type in a sentence:\n")

first_char = data[0]
last_char = data[-1]
first_char_count = data.count(first_char)
last_char_count = data.count(last_char)

fmt = "The {} character '{}' occurs {} time(s)"
print(fmt.format("first", first_char, first_char_count))
print(fmt.format("last", last_char, last_char_count))
