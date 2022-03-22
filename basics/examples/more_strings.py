#!/usr/bin/env python3

word = "is"
sentence = "The capital of Mississippi is Jackson."
position = sentence.find(word)
print("First:", position, "\t2nd: ", sentence.find(word, position + 1))
print(sentence.find(word, 8, 12))
print("The word '", word, "' appears", sentence.count(word), "times.\n")
print("Right Justified:", word.rjust(15), "|")
print(" Left Justified:", word.ljust(15, "*"), "|")

data = "1 4 1 1abc"
print("data:", data)
print("replace all:", data.replace("1", "0"))
print("replace two:", data.replace("1", "0", 2))

pieces = data.split(' ')
print(data)
print("pieces is of type:", type(pieces))
print(pieces)
