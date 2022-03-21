""" A Solution For classes_ex02
    Create a class called Family.
    • The Family does not extend Person but rather should be composed
      of two Person objects representing the parents and a list of Person
      objects representing the children.
    • Therefore, the __init__() method should take two required parameters
      (the parents), followed by a variable number of arguments (the children).
    • The following code can be used to test your classes.
            def main():
                mother = Person("Mom", 45, "F")
                father = Person("Dad", 45, "M")
                kid1 = Person("Johnie", 2, "M")
                kid2 = Person("Janie", 3, "F")
                myFamily = Family(mother, father, kid1, kid2)
                kid3 = Person("Paulie", 1, "M")
                myFamily.add(kid3)
                print(myFamily)

            if __name__ == "__main__":
                main()
    • Note the add method in the Family class.
"""


class Person:
    default = "Unknown"

    def __init__(self, name=default, age=1, gender=default):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return "{} {} {}".format(self.name, self.age, self.gender)


class Family:
    def __init__(self, parent1, parent2, *children):
        self.parent1 = parent1
        self.parent2 = parent2
        self.kids = list(children)

    def add(self, child):
        self.kids.append(child)

    def __str__(self):
        family = str(self.parent1) + " " + str(self.parent2)
        for kid in self.kids:
            family += "\n\t" + str(kid)
        return family


def main():
    mom = Person("Sally", 76, "F")
    dad = Person("Arthur", 62, "M")
    print(mom, dad)

    joel = Person("Joel", 41, "M")
    judy = Person("Judy", 38, "F")
    fam = Family(mom, dad, joel, judy)
    print("*** Family Members are")
    print(fam)
    print()
    mike = Person("Michael", 33, "M")
    fam.add(mike)
    print("*** Family Members are")
    print(fam)


if __name__ == "__main__":
    main()
