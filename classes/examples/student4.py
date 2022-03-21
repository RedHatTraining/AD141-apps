#!/usr/bin/env python3
class Student:

    def __init__(self, name, major):
        self.name = name    # Calls the @name.setter method
        self.major = major  # Calls the @major.setter method

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def major(self):
        return self._major

    @major.setter
    def major(self, major):
        self._major = major

    def __str__(self):
        return "{} : {}".format(self.name, self.major)

    def __eq__(self, obj):
        if type(obj) != Student:
            return False
        else:
            return self.name == obj.name and \
                   self.major == obj.major
