#!/usr/bin/env python3
def main():
    with open(input("Enter a file name: "), "r") as the_file:
        for a_line in the_file:
            print(a_line, end="")


if __name__ == "__main__":
    main()
