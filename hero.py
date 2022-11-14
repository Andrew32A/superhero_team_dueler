import random

class Hero:
    def __init__(self, name, starting_health=100):
        '''Instance properties:
        name: string
        starting_health: interger
        current_health: interger
        '''

        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def fight(self, opponent):
        """ Current hero will take turns fighting the opponent hero passed in """
        random_num = random.randint(0,1)

        if random_num == 0:
            print(f"{opponent.name} wins!")
        
        else:
            print(f"{self.name} wins!")


if __name__ == "__main__":
    my_hero = Hero("Grace Hopper", 200)
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")

    hero1.fight(hero2)



    print(my_hero.name)
    print(my_hero.current_health)

