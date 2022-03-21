#!/usr/bin/env python3
import os


def main():
    fmt = "CursorStart:{:<3}  Offset:{:<3}  Read:{:<3} " +\
          "CursorEnd:{:<3}  Data:{}"
    # Reading from file in binary mode
    with open("seekdata.txt", "rb") as f:
        offset, whence, chunk = (-20, os.SEEK_END, 5)
        f.seek(0, whence)
        start = f.tell()
        f.seek(offset, whence)
        data = f.read(chunk)
        print(fmt.format(start, offset, chunk, f.tell(), data))

        offset, whence, chunk = (3, os.SEEK_CUR, 7)
        start = f.tell()
        f.seek(offset, whence)
        data = f.read(chunk)
        print(fmt.format(start, offset, chunk, f.tell(), data))


if __name__ == "__main__":
    main()
