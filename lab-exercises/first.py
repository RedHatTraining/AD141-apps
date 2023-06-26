#!/usr/bin/env python3

print("Hello Variables")

x = 50
y = "50"
z = 50.0

print("X, Y, Z! Reveal yourselves!\n")
tab = " \t"

print(x, tab, type(x), tab, id(x))
print(y, tab, type(y), tab, id(y))
print(z, tab, type(z), tab, id(z))

print("X and Y Combine! Form A!\n")
a = x + int(y) 

print("Reveal!")
print(a, tab, type(a), tab, id(a))

