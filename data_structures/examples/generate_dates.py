#!/usr/bin/env python3
import datetime


def following_days(howmany):
    now = datetime.date.today()
    for i in range(1, howmany + 1):
        yield now + datetime.timedelta(days=i)


def main():
    print("Code was run on:", datetime.date.today())
    print("Next 7 days are:")
    for adate in following_days(7):
        print(adate)


if __name__ == "__main__":
    main()
