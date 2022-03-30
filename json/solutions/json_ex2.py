#!/usr/bin/env python3
'''
json_ex2.py

Write a program that saves a dictionary as a JSON file.
The dictionary should contain the word frequency
  (words as keys, frequency as values) read from the ch1_cyclone file.
When saving the JSON file, the indentation level should be tab characters.
The program should display the word that appeared most often in the file.
'''

import json


def main():
    word_frequency = {}
    max_count = 0
    max_word = ""
    with open("cyclone", "r") as data:
        for line in data:
            for word in line.split():
                count = word_frequency.get(word, 0) + 1
                word_frequency[word] = count
                if count > max_count:
                    max_count = count
                    max_word = word

    with open("frequencies.json", "w") as frequency:
        json.dump(word_frequency, frequency, indent="\t")

    print("'{}' occured {} times".format(max_word, max_count))


if __name__ == "__main__":
    main()
