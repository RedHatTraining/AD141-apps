#!/usr/bin/env python3
import datetime


def main():
    f = open('output', 'w')
    data = [1, 2, 3]
    today = datetime.datetime.today()
    # f.write(today)  ~ Will not work since not a string
    f.write(str(data) + "\n")
    f.write(str(today) + "\n")
    f.close()


if __name__ == "__main__":
    main()
