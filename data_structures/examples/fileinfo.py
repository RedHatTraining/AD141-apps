#!/usr/bin/env python3
import os


def main():
    files = os.listdir(".")
    fileinfo = {f: os.path.getsize(f) for f in files}
    for name, size in fileinfo.items():
        print("{0:30} : {1:>6,} bytes".format(name, size))


if __name__ == "__main__":
    main()
