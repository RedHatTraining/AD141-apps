#!/usr/bin/env python3
listA = list()
listB = []
listC = [20, 3, 7, 82, -3, 456, 3, 65, 23]
listD = ["James", "Heather", "Monica", "Eugene"]
listE = listC + listD
print(listA, listB, listC, listD, listE, sep="\n")
print("Indexing:", listC[0], listC[-1], listD[2], listE[4])
sub_list = listC[0:5]
print(type(sub_list), sub_list)
print(listE[-5:])
