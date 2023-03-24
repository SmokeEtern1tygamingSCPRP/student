from Lesson_2.character import Character
from colorama import Fore

class Vampyre(Character):
    def __init__(self, name='', health=1000, damage=40, defence=0, color=Fore.LIGHTBLUE_EX):
        Character.__init__(self, name, health, damage, defence, color)
        self.max_health = health

    def take_damage(self, damage):
        self.health -= max(damage, 0)

    def attack(self, target):
        dealt_damage = self.damage
        target.take_damage(self.damage)
        restored_health = int(dealt_damage * 0.1)
        self.health += restored_health
