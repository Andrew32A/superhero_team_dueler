import random

class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage

       
    def attack(self):
        """ Return a value between 0 and the value set by self.max_damage """
        return random.randint(0, self.max_damage)



if __name__ == "__main__":
    ability = Ability("debugging ability", 20)
    print(ability.name)
    print(ability.attack())