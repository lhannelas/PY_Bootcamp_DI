class Character:
    def __init__(self, name, life=20, attack=10):
        self.name = name
        self.life = life
        self.attack = attack

    def basic_attack(self, other_character):
        other_character.life -= self.attack
        print(f"{other_character.name} got hit by {self.attack} points. His remaining life is {other_character.life}")


class Druid(Character):
    def __init__(self, name):
        super().__init__(name)
        print("The Druid is among us")

    def meditate(self):
        self.life += 10
        self.attack -= 2
        print(f"{self.name} life has increased by 10 and is now {self.life}. {self.name} attack has decreased by"
              f" 2 and is now {self.attack}")

    def animal_help(self):
        self.attack += 5
        print(f"{self.name} attack has increased by 5 and is now {self.attack}")

    def fight(self, other_character):
        other_character.life -= (0.75 * self.life + 0.75 * self.attack)
        print(f"{other_character.name} has received a blow of {0.75 * self.life + 0.75 * self.attack} points."
              f" His remaining life is {other_character.life}")


class Warrior(Character):
    def __init__(self, name):
        super().__init__(name)
        print("You can hear the Warrior roar")

    def brawl(self, other_character):
        other_character.life -= 2 * self.attack
        self.life += 0.5 * self.attack
        print(
            f"{other_character.name} was hit by {2 * self.attack} points. His remaining life is {other_character.life}. "
            f"{self.name} life has increased by {0.5 * self.attack} points. Life is now at {self.life} points")

    def train(self):
        self.attack += 2
        self.life += 2
        print(f"{self.name} has increased his attack by 2 points. Attack is now at {self.attack}. "
              f"His life has also increased by 2 points. Life is now at {self.life}")

    @staticmethod
    def roar(other_character):
        other_character.attack -= 3
        print(
            f"{other_character.name} was scared. His attack dropped by 3 and is now at {other_character.attack} points")


class Mage(Character):
    def __init__(self, name):
        super().__init__(name)
        print("Brace yourself for magic")

    @staticmethod
    def curse(other_character):
        other_character.attack -= 2
        print(
            f"{other_character.name} has been cursed. His attack dropped by 3 and is now {other_character.attack} points")

    def summon(self):
        self.attack += 3
        print(f"{self.name} attack has increased by 3. It is now at {self.attack} points")

    def cast_spell(self, other_character):
        other_character.life -= self.attack // self.life
        print(f"{other_character.name} was hit by {self.attack // self.life} points. "
              f"His remaining life is {other_character.life} ")


druid = Druid("Laurent")
warrior = Warrior("Joeri")
mage = Mage("Angkush")

druid.basic_attack(warrior)
druid.fight(warrior)
druid.meditate()
druid.animal_help()

warrior.basic_attack(mage)
warrior.brawl(druid)
warrior.train()
warrior.roar(mage)

mage.curse(warrior)
mage.summon()
mage.cast_spell(warrior)
