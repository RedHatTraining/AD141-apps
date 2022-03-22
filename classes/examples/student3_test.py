#!/usr/bin/env python3
from student3 import Student


def main():
    jeff = Student("Jeff", "American History")
    heather = Student("Heather", "Mathematics")
    print(jeff.name, ":", jeff.major)
    jeff.name = "Jeffrey"
    print(jeff.name, ":", jeff.major)
    heather.major = "Computer Science"
    print(heather.name, ":", heather.major)


if __name__ == "__main__":
    main()
