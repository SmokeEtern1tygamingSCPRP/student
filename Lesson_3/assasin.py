from Lesson_2.character import Character
from colorama import Fore
import random


def roll(self, probability):
    return random.randint(0, 100) < probability


class Assasin(Character):
    def __init__(self, name='', health=700, damage=30, defence=0, color=Fore.LIGHTBLUE_EX):
        Character.__init__(self, name, health, damage, defence, color)
        self.max_health = health

    def take_damage(self, damage):
        self.health -= max(damage, 0)

    def attack(self, target):
        if random.random() < 0.3:  # вероятность 30% для нанесения 1000 урона
            return 100
        else:
            target.take_damage(self.damage)







