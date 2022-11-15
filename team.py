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