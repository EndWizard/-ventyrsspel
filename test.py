from typing import Pattern
from Testar import Weapon
from game import Player

name = input("\n\nWhat is your name travler? :")
rusty_sword = Weapon("Rusty Shortsword","It's a rusty old sword you found on the ground...",1)
player1 = Player(name)
player1.eqipped = rusty_sword
player1.inv.append(rusty_sword)


import random as rand
def stats(player1):
    print(player1.name)
    print(player1.lvl)