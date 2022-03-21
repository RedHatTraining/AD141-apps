#!/usr/bin/env python3
from fraction import Fraction


def main():
    fractions = [Fraction(1, 3), Fraction(), Fraction(3, 4)]
    for fraction in fractions:
        print(fraction)

    frac_1_3, frac_0_1, frac_3_4 = fractions
    print(frac_1_3, "<", frac_0_1, ":", frac_1_3 < frac_0_1)  # False
    print(frac_1_3, "<", frac_3_4, ":", frac_1_3 < frac_3_4)  # True
    result = frac_1_3 * frac_3_4
    print(frac_1_3, "*", frac_3_4, "=", result)  # 1/3 * 3/4 = 3/12


if __name__ == "__main__":
    main()
