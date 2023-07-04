#!/usr/bin/python3

text = input("This script will count the occurences of the first and \
last character input! Enter some text: ")

first_test = text.find(text[0]) 
second_test = text.find(text[-1])

print(import_test.divider)
print("The character " + text[0] + " appears a total of " + str(text.count(text[0])) + " times.")
print("The character " + text[-1] + " appears a total of " + str(text.count(text[-1])) + " times.")
