#!/usr/bin/env python3
def main():
    with open(input("Enter a file name: "), "r") as the_file:
        the_lines = the_file.readlines()
    for a_line in the_lines:
        print(a_line, end="")


if __name__ == "__main__":
    main()
