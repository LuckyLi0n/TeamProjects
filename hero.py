from gameunit import *

class Hero(Attacker):
    def __init__(self, name):
        self._name = name
        self._health = 100
        self._attack = 50
        self._experience = 0

    def attack(self, target):
        self.experience += 10
        target._health -= self._attack




































