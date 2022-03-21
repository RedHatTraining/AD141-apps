#!/usr/bin/env python3
""" This module defines a Student datatype and a main function to demonstrate
    the instantiation of a Student object """


class Student:
    """ This class represents a Student. This mulitline string will act as
    a doc string since it is declared at the top of the class"""


def main():
    """ This main is basically for testing purposes only.
    The Student class would typically be imported by
    another module as opposed to running it here."""

    jeff = Student()     # Instantiate a Student object
    heather = Student()  # Instantiate another Student
    print(jeff, id(jeff), hex(id(jeff)))
    print(heather, id(heather), hex(id(heather)))


if __name__ == "__main__":
    main()
