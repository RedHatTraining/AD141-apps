#!/usr/bin/env python3
import sys


def main():
    filename = sys.argv[1] if len(sys.argv) > 1 else input("Enter file name: ")
    f = open(filename, 'w')
    f.write('This is a test.\n')
    f.close()


if __name__ == "__main__":
    main()
