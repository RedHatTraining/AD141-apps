#!/usr/bin/env python3
""" A Solution For classes_ex01
    Create a class called Person.
    • Each Person should have a name, an age, and a gender.
    • In addition to getters and setters for the above methods,
      the Person class should have an __init__() method and a
      __str__() method.
    • The __init__() and __str__() methods should be defined such
      that  the following can be tested inside of an application.
            p1 = Person("Michael", 45, "M")
            print(p1)
"""


class Person:
    default = "Unknown"

    def __init__(self, name=default, age=1, gender=default):
        self.name = name
        self.age = age
        self.gender = gender

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, gender):
        self._gender = gender

    def __str__(self):
        return "{} {} {}".format(self.name, self.age, self.gender)


def main():
    mom = Person("Sally", 76, "F")
    dad = Person("Arthur", 62, "M")
    print(mom)
    print(dad)


if __name__ == "__main__":
    main()
