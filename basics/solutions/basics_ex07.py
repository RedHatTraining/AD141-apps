#!/usr/bin/env python3
""" A Solution For basics_ex07
    Write a program that prompts the user for a string and then prompts again
    for a number.
    • The program should create and print a new string by using the
      repetition operator on the string and the number.
    • For example, if the string is hello and the number is 3, then
      hellohellohello should be printed.
"""

data = input("Enter a string: ")
number = int(input("Enter a repetition factor: "))

repeat = data * number

print(data, "repeated", number, "times is:", repeat)
