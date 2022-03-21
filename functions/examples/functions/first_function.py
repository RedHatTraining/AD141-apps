#!/usr/bin/env python3
def print_with_border(some_text):
    border = len(some_text) * "#"
    print(border)
    print(some_text)
    print(border)


print_with_border("Hello")
print_with_border("Goodbye")
data = input("Enter some text: ")
print_with_border(data)
