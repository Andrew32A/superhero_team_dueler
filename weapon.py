from ability import Ability
import random

class Weapon(Ability):
    def attack(self):
        """
        this method returns a random value between one half to the full attack power of weapon
        """
        self.max_damage = random.randint(self.max_damage/2, self.max_damage)
        return self.max_damage
