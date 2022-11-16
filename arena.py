from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena:
    def __init__(self):
        """
        instantiate properties
        team_one: none
        team_two: none
        """
        self.team_one = []
        self.team_two = []

    def create_ability(self):
        """
        prompt for Abilitiy information, return Ability with values from user input
        """
        name = input("What is the ability name? ")
        max_damage = input("What is the max damage of the ability? ")

        return Ability(name, max_damage)

    def create_weapon(self):
        """
        prompt the user for Weapon information, return Weapon with values from user input
        """
        name = input("What is the weapon name? ")
        max_damage = input("What is the max damage of the weapon? ")

        return Weapon(name, max_damage)

    def create_armor(self):
        """
        prompt user for Armor information, return Armor with values from user input
        """
        name = input("What is the armor name? ")
        self_block = input("What is the defense power of the armor? ")

        return Armor(name, self_block)

    def create_hero(self):
        """
        prompt user for Hero information, return Hero with values from user input
        """
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
            add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
            if add_item == "1":
                hero.add_ability(self.create_ability())

            elif add_item == "2":
                hero.add_weapon(self.create_weapon())

            elif add_item == "3":
                hero.add_armor(self.create_armor())

        return hero

    def build_team_one(self):
        """
        prompt the user to build team_one
        """
        num_of_team_members = int(input("How many members would you like one Team One?\n"))
        for i in range(num_of_team_members):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

            
    def build_team_two(self):
        """
        prompt the user to build team_two
        """
        num_of_team_members = int(input("How many members would you like one Team Two?\n"))
        for i in range(num_of_team_members):
            hero = self.create_hero()
            self.team_two.add_hero(hero)

    def team_battle(self):
        """
        battle team_one and team_two together
        """
        self.team_one.attack(self.team_two)    

    def show_stats(self):
        '''prints team statistics to terminal.'''
        print("\n")
        print(self.team_one.name + " statistics: ")
        self.team_one.stats()
        print("\n")
        print(self.team_two.name + " statistics: ")
        self.team_two.stats()
        print("\n")

        team_kills = 0
        team_deaths = 0
        for hero in self.team_one.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
        if team_deaths == 0:
            team_deaths = 1
        print(self.team_one.name + " average K/D was: " + str(team_kills/team_deaths))

        for hero in self.team_one.heroes:
            if hero.deaths == 0:
                print("survived from " + self.team_one.name + ": " + hero.name)

        for hero in self.team_two.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
        if team_deaths == 0:
            team_deaths = 1
        print(self.team_two.name + " average K/D was: " + str(team_kills/team_deaths))

        for hero in self.team_two.heroes:
            if hero.deaths == 0:
                print("survived from " + self.team_two.name + ": " + hero.name)
                

if __name__ == "__main__":
    game_is_running = True

    # instantiate Game Arena
    arena = Arena()

    #build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()