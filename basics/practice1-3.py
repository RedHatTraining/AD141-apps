#!/usr/bin/python3

print("Welcome to the text evaluation exercise.\n" + 
        "This script will evaluate your text for the following: \n" +
        "    1. If it ends in a period.\n" + 
        "    2. If it contains all alphabetic characters. \n" +
        "    3. If there is the character \"x\" in your text.\n" + 
        "All tests will be evaluated as True or False, and all instances of the letter e will be capitalized to the letter \"E.\"")

text = input("Enter text to evauluate: ")
divider = "#" * 15

print(divider)

test_1_result = str(text.endswith("."))
test_2_result = str(text.isalnum())
test_3_result = str(bool("x" in text))
new_text = text.replace("e", "E")

print("Test 1: " + test_1_result)
print("Test 2: " + test_2_result)
print("Test 3: " + test_3_result)
print("Your new text is: " + new_text)
print(divider)
