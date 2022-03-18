#!/usr/bin/env python3
word = "Hello"
print(word)
for each_character in "Hello":
    print(each_character, end="\t")

delim = "\n\t"
print("\nrange(5):", end=delim)
for i in range(5):
    print(i, end=" ")

print("\nrange(5, 10)", end=delim)
for i in range(5, 10):
    print(i, end=" ")

print("\nrange(-5, 9, 3)", end=delim)
for i in range(-5, 9, 3):
    print(i, end=" ")

print()
