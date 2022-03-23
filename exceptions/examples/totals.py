#!/usr/bin/env python3
def main():
    total = 0
    msg = "Please enter a number, or 'end' to quit: "
    while True:
        value = input(msg)
        if value == "end":
            break
        total += int(value)

    print("Total is", total)


if __name__ == "__main__":
    main()
