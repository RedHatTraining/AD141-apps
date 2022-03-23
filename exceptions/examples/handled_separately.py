#!/usr/bin/env python3
def main():
    total = 0
    while True:
        try:
            value = input("Please enter a number: ")
            if value == "end":
                break
        except EOFError:
            print('Unexpected End of Stream')
            continue
        try:
            total += int(value)
        except ValueError as ve:
            print("Exception: ", ve)
        finally:
            print("Running subtotal is:", total)

    print("Total is", total)


if __name__ == "__main__":
    main()
