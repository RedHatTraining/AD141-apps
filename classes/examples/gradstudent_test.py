#!/usr/bin/env python3
from gradstudent import GradStudent


def main():
    grad_student = GradStudent("James", "Anthropology", 25000)

    print("  MAJOR:", grad_student.major)
    print("   NAME:", grad_student.name)
    print("STIPEND:", grad_student.stipend)
    print(grad_student)


if __name__ == "__main__":
    main()
