#!/usr/bin/env python3
import string


def main():
    try:
        with open("alphabet", "w") as the_file:
            the_file.write(string.ascii_letters)
        print("The following was written to the file:")
        print(string.ascii_letters, "\n")

        with open("alphabet", "r") as the_file:
            while True:
                the_text = the_file.read(10)
                if not the_text:
                    break
                print(the_text)
    except OSError as err:
        print("IO Error:", err)


if __name__ == "__main__":
    main()
