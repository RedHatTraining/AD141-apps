#!/usr/bin/env python3
"""Functiion to return a list with elements common to both lists"""
def find_common(list_a, list_b):
    setA = set(list_a)
    setB = set(list_b)
    return list(setA & setB)

first = "A B c d e F G H".split()
second ="d e H B I J K L".split()
result = find_common(first, second)
print(type(result))
print("Function returns:",result)
