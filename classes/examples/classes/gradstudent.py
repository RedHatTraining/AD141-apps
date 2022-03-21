#!/usr/bin/env python3
from student4 import Student


class GradStudent(Student):

    def __init__(self, name, major, stipend):
        # Pass the name and major to the __init__() of the
        # super class then store the part specific to the
        # GradStudent object
        super().__init__(name, major)
        self.stipend = stipend

    @property
    def stipend(self):
        return self._stipend

    @stipend.setter
    def stipend(self, stipend):
        self._stipend = stipend

    def __str__(self):
        # Override the __str__ from the parent class by
        # first getting the parent information:
        # super().__str__()
        # and then concatenating the stipend
        return "{} {}".format(super().__str__(), self.stipend)
