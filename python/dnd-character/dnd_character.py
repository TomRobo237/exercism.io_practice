from os import urandom
from random import seed, randint, choice
from math import floor

seed(urandom(10))

STATS = ['strength',
         'dexterity',
         'constitution',
         'intelligence',
         'wisdom',
         'charisma']

def modifier(stat):
    return int(floor((stat - 10) / 2))

class Character:
    def ability(self):
        rolls = [randint(1,6) for _ in range(0,4)]
        rolls.remove(min(rolls))
        return sum(rolls)
    def __init__(self):
        for i in STATS:
            setattr(self, i, self.ability())
        self.hitpoints = 10 + modifier(self.constitution)

