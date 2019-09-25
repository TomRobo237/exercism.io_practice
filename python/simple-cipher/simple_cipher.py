from random import SystemRandom
from string import ascii_lowercase
from itertools import cycle


class Cipher(object):
    def __init__(self, key=None):
        if key is None:
            self.key = []
            [self.key.append(SystemRandom().choice(ascii_lowercase)) for _ in range(0, 101)]
            self.key = ''.join(self.key)
        else:
            self.key = key
        self.shifts = [ord(x) - 97 for x in list(self.key)]

    def encode(self, text):
        return ''.join(
            [ascii_lowercase[(ascii_lowercase.index(x) + y) % len(ascii_lowercase)]
             for x, y in zip(list(text), cycle(self.shifts))])

    def decode(self, text):
        return ''.join(
            [ascii_lowercase[(ascii_lowercase.index(x) - y) % len(ascii_lowercase)]
             for x, y in zip(list(text), cycle(self.shifts))])
