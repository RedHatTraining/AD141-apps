#!/usr/bin/env python3
def print_score(player, **scores):
    total_score = 0
    print("Player:", player)
    for category, score in scores.items():
        print("{0:>15}: {1}".format(category, score))
        total_score += score
    print("{0:>15}: {1}".format("Total", total_score))


print_score("Aiden", Aces=4, Twos=8, FullHouse=25, LgStraight=40)
print_score("Cindy", Twos=4, LgStraight=40, Chance=24, ThreeOfAKind=21)
