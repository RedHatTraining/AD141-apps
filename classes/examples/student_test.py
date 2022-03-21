#!/usr/bin/env python3
from student4 import Student


def main():
    s1 = Student("Elizabeth", "Electrical Engineering")
    s2 = Student("Robert", "Electrical Engineering")
    student_info("Before", s1, s2)
    s2.name = "Elizabeth"
    student_info("After", s1, s2)


def student_info(label, student1, student2):
    print(label)
    print(student1, "id=", id(student1))
    print(student2, "id=", id(student2))
    fmt = "{0} == {1} : {2}"
    print(fmt.format(student1, student2, student1 == student2))
    print()


if __name__ == "__main__":
    main()
