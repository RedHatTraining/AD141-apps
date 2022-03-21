#!/usr/bin/env python3
numbers = [3, 1, -10, 54, 75, 29]
words = ["Hello", "Goodbye", "goodbye", "hello"]
label1, label2 = ("  Unsorted:", "  Sorted:")
print("Basic sorting of a list.")
print(label1, numbers, words)
numbers.sort()
words.sort()
print(label2, numbers, words, "\n")
numbers = [3, 1, -10, 54, 75, 29]

print("Basic sorting of a list in reverse.")
print(label1, numbers, words)
numbers.sort(reverse=True)
words.sort(reverse=True)
print(label2, numbers, words, "\n")
