from assasin import Assasin
from samurai import Samurai
from ninja import Ninja
from vampyre import Vampyre
from colorama import Fore

print('Красные юниты - Красныя команда')
print('Синие юниты - Синяя команда')

player1 = Assasin(name='Эцио', health=700, damage=30, defence=0,
                    color=Fore.LIGHTRED_EX)
print(player1)

player2 = Samurai(name='武士', health=1000, damage=10, defence=0,
                    color=Fore.LIGHTBLUE_EX)
print(player2)

player3 = Ninja(name='Ninjaon', health=900, damage=50, defence=0,
                    color=Fore.LIGHTMAGENTA_EX)
print(player3)

player4 = Vampyre(name='Drakula', health=1000, damage=30, defence=0,
                    color=Fore.LIGHTCYAN_EX)
print(player4)

while player1.is_alive() and player2.is_alive():
    player1.attack(player2)
    player2.attack(player1)


    print(player1)
    print(player2)


while player3.is_alive() and player4.is_alive():
    player3.attack(player4)
    player4.attack(player3)
    print(player3)
    print(player4)