#!/usr/bin/env python3
class Student:
    def __init__(self, name, major):
        self._name = name
        self._major = major

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_major(self):
        return self._major

    def set_major(self, major):
        self._major = major


def main():
    jeff = Student("Jeff", "American History")
    print(jeff.get_name(), ":", jeff.get_major())
    jeff.set_name("Jeffrey")
    print(jeff.get_name(), ":", jeff.get_major())


if __name__ == "__main__":
    main()
