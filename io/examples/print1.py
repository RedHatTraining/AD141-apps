#!/usr/bin/env python3
from datetime import datetime


def main():
    f = open("output", "w")
    cnt = 1
    while True:
        data = input("Enter data ('q' to exit): ")
        if data == "q":
            break
        txt = "{:04}".format(cnt)
        print(txt, datetime.today(), data, file=f)
        cnt += 1
    f.close()


if __name__ == "__main__":
    main()
