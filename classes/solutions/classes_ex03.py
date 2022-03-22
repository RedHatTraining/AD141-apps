""" A Solution For classes_ex03
    Implement the necessary special methods so that the <, ==, and >
    operators can be used with Family objects.
    • The criteria for the methods should be the number of children.
    • The following code could be used to test the methods.
            myFamily = Family(mom, dad, kid1, kid2)
            smiths = Family(mom, dad, kid1)
            if (myFamily > smiths):
                print("we have more kids than smiths")
            if (myFamily == smiths):
                print("families have same # of kids")
            if (myFamily < smiths):
                print("we have fewer kids than smiths")
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

    def __gt__(self, other):
        return len(self.kids) > len(other.kids)

    def __eq__(self, other):
        return len(self.kids) == len(other.kids)

    def __lt__(self, other):
        return len(self.kids) < len(other.kids)


def main():
    mom = Person("Sally", 76, "F")
    dad = Person("Arthur", 62, "M")
    joel = Person("Joel", 34, "M")
    judy = Person("Judy", 35, "F")
    fam1 = Family(mom, dad, joel, judy)
    fam2 = Family(mom, dad, joel)

    if fam1 > fam2:
        print("fam1 has more kids than fam2")

    fam2.add(judy)

    if fam1 == fam2:
        print("families have == number of kids")

    fam2.add(Person("Aiden", 13, "M"))

    if fam1 < fam2:
        print("fam1 has fewer kids than fam2")


if __name__ == "__main__":
    main()
