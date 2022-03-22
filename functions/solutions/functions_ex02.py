#!/usr/bin/env python3
""" A Solution For functions_ex02
    Write and test a function that takes a collection of strings and
    returns thelength of the longest string in the collection.
    • The application should loop through the collection of strings and
      rely on the value returned by the function to format all of the strings
      to the output such that they are all right justified to the width of
      the longest string.
"""


def get_max_length(data):
    return len(max(data, key=len))


words = ["hello", "supercalafragalistic", "Q", "moose", "functions!"]
longest = get_max_length(words)

for word in words:
    print(f"{word:>{longest}s}")
