import random

class Team():
    def __init__(self, name):
        """
        initialize your team with its team name and an empty list of heroes
        """
        self.name = name
        self.heroes = list()


    def remove_hero(self, name):
        """
        remove hero from heroes list, if hero isn't found return 0
        """
        found_hero = False

        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                found_hero = True


        if not found_hero:
            return 0

    def view_all_heroes(self):
        """
        prints out all heroes to the console
        """
        for hero in self.heroes:
            print(f"Hero name: {hero.name}")

    def add_hero(self, hero):
        """
        add hero object to self.heroes.
        """
        self.heroes.append(hero)

    def stats(self):
        """
        print team statistics
        """
        # could not divide by zero, so I had to remove k/d
        for hero in self.heroes:
            # kd = hero.kills / hero.deaths
            print(f"{hero.name} Kill/Deaths: {hero.kills}/{hero.deaths}")

    def revive_heroes(self, health=100):
        """
        reset all heroes to starting_health
        """
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def attack(self, other_team):
        """
        battle each team against each other
        """
        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents) > 0:
            fighting_hero = random.choice(living_heroes)
            fighting_opponent = random.choice(living_opponents)

            fighting_hero.fight(fighting_opponent)

            if fighting_hero.current_health < 0:
                living_heroes.remove(fighting_hero)

            elif fighting_opponent.current_health < 0:
                living_opponents.remove(fighting_opponent)
            
            else:
                pass

        self.stats()
        other_team.stats()

        if len(living_heroes) >= 0:
            print(f"{self.name} won!!")

        elif len(living_opponents) >= 0:
            print(f"{other_team.name} won!!")