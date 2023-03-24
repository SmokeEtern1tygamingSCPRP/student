from character import Character
from colorama import Fore



player1 = Character(name='Vasya', health=70, damage=10, defence=0,
                    color=Fore.LIGHTRED_EX)
print(player1)

player2 = Character(name='Petya', health=70, damage=10, defence=0,
                    color=Fore.LIGHTBLUE_EX)

while player1.is_alive() and player2.is_alive():
    player1.attack(player2)
    player1.attack(player1)



print(player1)
print(player2)

