#!/usr/bin/env python3
def main():
    char_count = line_count = 0
    with open(input("Enter a file name: "), "r") as a_file:
        while True:
            txt = a_file.readline()
            if not txt:
                break
            char_count += len(txt)
            line_count += 1

    print("Characters:", char_count, " Lines:", line_count)


if __name__ == "__main__":
    main()
