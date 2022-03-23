#!/usr/bin/env python3
import re
from regex_testing import getinput


def print_details(m):
    headers = ("#", "Start", "End", "Span", "Text")
    fmt = "{} {:^7}{:^7}{:^10} {}"
    print(fmt.format(*headers))
    # Group 0
    print(fmt.format(0, m.start(0), m.end(0), str(m.span(0)), m.group(0)))
    # Group 1 to the Number of groups
    # Note use of value of 1 as starting enumerate value
    for idx, a_group in enumerate(m.groups(), 1):
        print(fmt.format(idx, m.start(idx), m.end(idx),
                         str(m.span(idx)), a_group))


def main():
    previous_regex = ""
    print("Enter 'quit' at any time to quit the program")
    while True:
        the_tuple = getinput(previous_regex)
        if the_tuple:
            regex, text = the_tuple
            x = re.search(regex, text)
            if x:
                print_details(x)
                print()
            else:
                print("No Match found\n")
            previous_regex = regex
        else:
            break


if __name__ == "__main__":
    main()
