#!/usr/bin/env python3
from shape import Shape


class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width

    def __str__(self):
        fmt = "{}  Length:{} Width:{}"
        return fmt.format(super().__str__(), self.length,
                          self.width)

    def area(self):
        return self.length * self.width
