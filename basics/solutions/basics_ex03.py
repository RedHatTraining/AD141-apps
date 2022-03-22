#!/usr/bin/env python3

""" A Solution For basics_ex03
    Write a program that accepts a string from the user.
    • Determine and print the following information about the string:
    • Does it end in a period?
    • Does it contain all alphabetic characters?
    • Is there an 'x' in the string?
    • Create and print a new string that has all occurrences of 'e' changed
      to 'E'.
"""

data = input("Enter some text: ")

print("Ends with a period?", data.endswith("."))
print("Is all alpha?", data.isalpha())
print("Is 'x' in the text?", 'x' in data)
print()

original = 'e'
replacement = original.upper()
replaced = data.replace(original, replacement)
print("The text with all occurrences of", original, "replaced with",
      replacement)
print(replaced)
