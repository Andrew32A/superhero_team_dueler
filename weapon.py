from ability import Ability
import random

class Weapon(Ability):
    def __init__(self, name, max_damage):
        super(Weapon, self).__init__(name, max_damage)

    def attack(self):
        """
        this method returns a random value between one half to the full attack power of weapon
        """
        return random.randint(self.max_damage // 2, self.max_damage)
