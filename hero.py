import random
from ability import Ability
from armor import Armor
from weapon import Weapon

class Hero:
    def __init__(self, name, starting_health=100):
        '''Instance properties:
        abilities: list
        armors: list
        name: string
        starting_health: interger
        current_health: interger
        '''

        # abilities and armors don't have starting values and are set to empty lists on init
        self.abilities = list()
        self.armors = list()
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

    def add_ability(self, ability):
        """ add ability to abilities list """

        # uses append method to add ability objects to list
        self.abilities.append(ability)

    def attack(self):
        ''' 
        calculate total damage from all ability attacks 
        return: total_damage: int
        '''
        total_damage = 0

        # loop though all hero abilities
        for ability in self.abilities:
            total_damage += ability.attack()

        return total_damage

    def add_armor(self, armor):
        """
        add armor to self.armors
        armor: armor object
        """
        self.armors.append(armor)
    
    def defend(self):
        """
        calculate the total block amount froma all armor blocks
        return: total_block: int
        """
        total_armor = 0

        for armor in self.armors:
            total_armor += armor.block()

        return total_armor

    def take_damage(self, damage):
        """
        updates self.current_health to reflect the damage minus the defense
        """
        damage_taken = damage - self.defend()
        if damage_taken > 0:
            self.current_health -= damage_taken
            print(f"{self.name} took {damage_taken} damage!")
        else:
            print(f"{self.name} didn't take any damage!")

    def is_alive(self):
        """
        return True or False depending on whether the hero is alive or not
        """
        if self.current_health <= 0:
            print(f"{self.name} has fainted!")
            return False
        else:
            return True

    def fight(self, opponent):
        """
        current hero will take turns fighting the oppenent hero passed in
        """
        while self.is_alive() == True and opponent.is_alive() == True:
            self.take_damage(opponent.attack())
            opponent.take_damage(self.attack())
            print(f"{self.name} has {self.current_health} hp and {opponent.name} has {opponent.current_health} hp")

        if self.is_alive == False:
            print(f"{self.name} won!")

        elif opponent.is_alive == False:
            print(f"{opponent.name} won!")

    def add_weapon(self, weapon):
        """
        add weapon to self.abilities
        """
        self.abilities.append(weapon)


    

        


if __name__ == "__main__":
    # only runs code when in current file

    hero = Hero("wonder woman")
    weapon = Weapon("lasso of truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())
    
    
    
    
    # hero1 = Hero("wonder woman")
    # hero2 = Hero("dumbledore")
    # ability1 = Ability("super speed", 300)
    # ability2 = Ability("super eyes", 130)
    # ability3 = Ability("wizard wand", 80)
    # ability4 = Ability("wizard beard", 20)
    # hero1.add_ability(ability1)
    # hero1.add_ability(ability2)
    # hero2.add_ability(ability3)
    # hero2.add_ability(ability4)
    # hero1.fight(hero2)


    # ability = Ability("great debugging", 50)
    # ability2 = Ability("great debugging 2", 90)
    # shield = Armor("shield", 50)
    # hero = Hero("Grace Hopper", 200)
    # hero.add_ability(ability)
    # hero.add_ability(ability2)
    # hero.add_armor(shield)
    # print(hero.is_alive())
    # hero.take_damage(500000)
    # print(hero.is_alive())
    # print(hero.current_health)
    # print(hero.attack())

    # hero1 = Hero("Wonder Woman")
    # hero2 = Hero("Dumbledore")

    # hero1.fight(hero2)



    # print(my_hero.name)
    # print(my_hero.current_health)

