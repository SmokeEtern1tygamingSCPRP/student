from Lesson_2.character import Character
from colorama import Fore

class Samurai(Character):
    def __init__(self, name='', health=1000, damage=10, defence=0, color=Fore.LIGHTBLUE_EX):
        Character.__init__(self, name, health, damage, defence, color)
        self.max_health = health
        self.multiplier = 0

    def take_damage(self, damage):
        self.health -= max(damage, 0)


    def attack(self, target):
        self.multiplier += 0.1
        if self.multiplier > 0.5:
            self.multiplier = 0
        target.take_damage(self.damage * (1 + self.multiplier))


