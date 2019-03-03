# Score categories
# Change the values as you see fit
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):
    if category == 0 and all(x == dice[0] for x in dice):
            return 50
    if category in range(1,7): # ones through sixes
        return sum([ i for i in dice if i == category ])
    if category == 7 and (dice.count(sorted(dice)[0]) == 3 and dice.count(sorted(dice)[3]) == 2) \
            or (dice.count(sorted(dice)[0]) == 2 and dice.count(sorted(dice)[2]) == 3):
        return sum(dice)
    if category == 8 and (dice.count(sorted(dice)[0]) >= 4 or dice.count(sorted(dice)[1]) >= 4):
            return ( max(set(dice), key=dice.count) * 4 )
    if category == 9 and sorted(dice) == list(range(1,6)):
        return 30
    if category == 10 and sorted(dice) == list(range(2,7)):
        return 30
    if category == 11:
        return sum(dice)
    return 0
