# coding: utf-8
# license: GPLv3
from gameunit import *


class Hero(Attacker):
    name = ''
    experience = 0

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_strength = 50

    def attack(self, target):
        self.experience += 1
        Attacker.attack(self, target)




































