# coding: utf-8
# license: GPLv3


class Attacker:
    health = None
    attack_strength = None

    def attack(self, target):
        target.health -= self.attack_strength
        print(target.health)

    def is_alive(self):
        return self.health > 0
