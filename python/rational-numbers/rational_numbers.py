from __future__ import division

def reduceBy(a, b):
    '''Taken from fractions stdlib module'''
    while b:
        a, b = b, a % b
    return a

class Rational(object):
    def __init__(self, numer, denom):
        if denom == 0:
            raise ZeroDivisionError
        reduceby = reduceBy(numer, denom)
        self.numer = int(numer / reduceby)
        self.denom = int(denom / reduceby)

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        a = self.numer * other.denom + self.denom * other.numer
        b = self.denom * other.denom
        return Rational(a, b)

    def __sub__(self, other):
        a = self.numer * other.denom - self.denom * other.numer
        b = self.denom * other.denom
        return Rational(a, b)
        
    def __mul__(self, other):
        a = self.numer * other.numer
        b = self.denom * other.denom
        return Rational(a, b)

    def __truediv__(self, other):
        if other.numer == 0:
            raise ZeroDivisionError
        a = self.numer * other.denom
        b = self.denom * other.numer
        return Rational(a, b)

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        a = self.numer ** abs(power)
        b = self.denom ** abs(power)
        return Rational(a, b)

    def __rpow__(self, base):
        a = base ** self.numer
        b = 1 / self.denom
        return a ** b
        
