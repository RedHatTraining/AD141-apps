#!/usr/bin/env python3
from datetime import datetime, timedelta


def main():
    end = "\n\n"
    now = datetime.today()
    print("Today is:", now)
    print(now.month, now.day, now.year, sep="/", end=end)

    delta = timedelta(days=1, hours=12)
    future = now + delta
    print("36 hours from now:", future, end=end)

    past = datetime(2000, 1, 31, 14, 25, 59)
    print("A date in the past:", past, end=end)


if __name__ == "__main__":
    main()
