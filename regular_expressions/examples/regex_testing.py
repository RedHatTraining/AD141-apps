#!/usr/bin/env python3
import re


def getinput(regex):
    prompt = "Enter a RegEx or (<enter> to reuse previous):"
    prevregex = regex
    regex = input(prompt)
    if not regex:
        regex = prevregex
    elif regex == "quit":
        return tuple()
    line = input("Enter a string to search: ")
    if line == "quit":
        return tuple()
    return (regex, line)


def main():
    previous_regex = ""
    print("Enter 'quit' at any time to quit the program")
    while True:
        the_tuple = getinput(previous_regex)
        if the_tuple:
            regex, text = the_tuple
            x = re.search(regex, text)
            if x:
                print(x, "\n")
            else:
                print("No Match found\n")
            previous_regex = regex
        else:
            break


if __name__ == "__main__":
    main()
