from Lesson_2.character import Character
from colorama import Fore
import random

class Ninja(Character):
    def __init__(self, name='', health=900, damage=50, defence=0, color=Fore.LIGHTBLUE_EX):
        Character.__init__(self, name, health, damage, defence, color)
        self.max_health = health

    def take_damage(self, damage):
        if random.random() < 0.2:  # вероятность 20% для полного избежания урона
            return 0
        else:
            self.health -= max(damage, 0)


    def attack(self, target):
        target.take_damage(self.damage)

