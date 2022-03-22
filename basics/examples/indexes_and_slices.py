#!/usr/bin/env python3
spam = "Spam and eggs"
delim = " | "
# Indexing
print(spam[0], spam[3], spam[-1], spam[-4], sep=delim)

# Slicing
print(spam[2:7], spam[5:], spam[:8], sep=delim)

# Slicing from end
print(spam[-3:-1], spam[-3:], spam[:-1], sep=delim)
print()

# Extended Slicing
alphabet = "abcdefghijklmnopqrstuvwxyz"
print(alphabet[2:18:3])
start = 18
print(alphabet[start::1])
print(alphabet[::1])
