import random

class Armor:
    def __init__(self, name, self_block):
        """ 
        instantiate instance properties
        name: String
        max_block: Interger
        """

        self.name = name
        self.self_block = self_block

    def block(self):
        """ returns a random value between  and the initialized max_block strength """

        random_value = random.randint(0, self.self_block)
        return random_value


if __name__ == "__main__":
    Armor = Armor("debugging shield", 10)
    print(Armor.name)
    print(Armor.block())