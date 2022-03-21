#!/usr/bin/env python3
class Shape:
    id = 100

    def __init__(self, name):
        self.name = name
        self.number = Shape.id
        Shape.id += 1

    def area(self):
        pass  # Intended to be implemented by subclasses

    @property
    def name(self): return self._name

    @name.setter
    def name(self, name): self._name = name

    def __str__(self):
        return "Name:{}  id:{}".format(self.name, self.number)
