#!/usr/bin/env python3
def main():
    total = 0
    while True:
        value = input("Please enter a number: ")
        if value == "end":
            break
        try:
            total += int(value)
        except ValueError:
            print("Invalid Number - Please try again")

    print("Total is", total)


if __name__ == "__main__":
    main()
