#!/usr/bin/env python3
from shape_rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, name, length):
        super().__init__(name, length, length)
