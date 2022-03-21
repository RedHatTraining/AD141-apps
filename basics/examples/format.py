#!/usr/bin/env python3
separator = "----------------------------"
name = "First: {} \tLast Name: {} \tMiddle Initial: {}"
formatted = name.format("John", "Smith", "C.")
print(formatted)
formatted = name.format("Melony", "Jones", "A.")
print(formatted)
print(separator)

name = "{1},  {0}"
print(name.format("First", "Last"))
print(name.format("John", "Smith"))
print(name.format("Melony", "Jones"))
print(separator)

dimensions = "Type: {type}\nHeight:{height}, Width:{width}"
result = dimensions.format(height=50, width=25, type="Box")
print(result)
