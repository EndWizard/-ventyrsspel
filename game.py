import random as rand
import time
from monster_room import monster_room, battle_room
from backpack import backpack
from loot import item_room
from trap import trap_room
from Classes import Player, Potion, Weapon


#Theese two are gonna be for saving the game and stuff (exciting)

def intro():
    while True:
        title = input("Skip title screen? [y/n] :").casefold()
        if title == "n":
            f = open("title_card.txt")
            lines = f.readlines()
            for i in range(len(lines)):
                content = lines[i].strip("\n")
                print(content)
                time.sleep(0.5)
            f.close
            break
        elif title == "y":
            print("")
            break
        else:
            print("invalid input")

    name = input("\n\nWhat is your name traveler? :")
    rusty_sword = Weapon("Rusty Shortsword","It's a rusty old sword you found on the ground...",1)
    player1 = Player(name)
    player1.eqipped = rusty_sword
    player1.inv.append(Potion("torch","Its dark to go alone, take this!"))
    player1.inv.append(rusty_sword)
    player1.inv[0].type = "torch"
    time.sleep(1)
    print("\nYou find yourself in a dark room.")
    time.sleep(1)
    print("A flickering torch is sitting on the wall, you grab it\n")
    time.sleep(1)
    main_room(player1)

def main_room(player1):
    
    #If you're not dead (wich you proabably are) this will be the main menu
    while player1.HP >= 1 and player1.LVL <= 9 and player1.inv[0].type=="torch":
        #Generates the doors, if the player has one HP left they can't get a trap (cuz that would kinda suck)
        if player1.HP > 1:
            door1 = rand.randint(1,3)
            door2 = rand.randint(1,3)
            door3 = rand.randint(1,3)
        else:
            door1 = rand.randint(1,2)
            door2 = rand.randint(1,2)
            door3 = rand.randint(1,2)

        print("\n~~~Dungeon room~~~\n\n1 Explore [E]    2 Check stats [S]\n3 Check backpack [B]")
        goto = input("\nSelect menu option :").lower()
        #Each of the menu options sends you away to a different function
        if goto == "e":
            time.sleep(1)
            print("\n you approach three doors.")
            time.sleep(1)
            if player1.x_ray==True:
                rooms= ["chest standing on a pedestal","monster wandering around","weird mechanism that seems strangely intimidating"]
                print(f"\nbehind the left door you see a {rooms[door1-1]}")
                time.sleep(1)
                print(f"behind the middle door you see a {rooms[door2-1]}")
                time.sleep(1)
                print(f"behind the right door you see a {rooms[door3-1]}\n")
                time.sleep(1)
                player1.x_ray=False
            door = input("Wich one will you choose? [Left/Middle/Right] :").lower()
            if door == "left" or door == "l":
                time.sleep(1)
                door_ascii()
                print("\nYou approach the left door.")
                time.sleep(1)
                print("\nIt makes a loud creaking sound as you push it open...")
                time.sleep(1)
                warp_room(player1, door1)
            elif door == "middle" or door == "m":
                time.sleep(1)
                print(door)
                door_ascii()
                print("\nYou approach the middle door.")
                time.sleep(1)
                print("\nIt makes a loud creaking sound as you push it open...")
                time.sleep(1)
                warp_room(player1,door2)
            elif door == "right" or door =="r":
                time.sleep(1)
                door_ascii()
                print("\nYou approach the door to the right.")
                time.sleep(1)
                print("\nIt makes a loud creaking sound as you push it open...")
                time.sleep(1)
                warp_room(player1,door3)
            else:
                print("invalid input!")
                time.sleep("2")
                return
        elif goto == "b":
            backpack(player1)
        elif goto == "s":
            stats(player1)
        else:
            print("invalid input!")
            time.sleep(2)
    endgame(player1)
#

def endgame(player1):
    if player1.HP <= 0:
        print(f"Well you had a good run {player1.name}")
        time.sleep(2)    
        print("...")
        time.sleep(2)
        print("...")
        time.sleep(2)
        print("The struggle for survival is over.")
        time.sleep(3)
        print("you can rest now.")
        time.sleep(3)
        print("\n\nGame Over")
    elif player1.HP > 0 and player1.LVL >= 10:
        print(f"Congrats {player1.name}, you beat the dungeon")
        time.sleep(3)
        print("The odds where against you, but you managed to pull through")
        time.sleep(3)
        print("you see it, the final door. Right by the end of the corridor.")
        time.sleep(3)
        print("you're finnaly strong enough to leave this wretched place.")
        time.sleep(3)
        print("Time stands still, you walk for what seems like an eternity")
        for i in range(3):
            time.sleep(2)
            print("...")
        time.sleep(2)
        print("You finnaly reach it.")
        time.sleep(1)
        print("It wont budge...")
        time.sleep(2)
        print("it cant be....")
        time.sleep(2)
        print("this was supposed to be it....")
        time.sleep(2)
        print("a trapdoor flings open, sending you down in to darkness")
        time.sleep(3)
        print("\n\nWhen you open your eyes, the first thing you see is blue.")
        time.sleep(3)
        print("Its the sky...")
        time.sleep(2)
        print("you quickly stand up and look around. you're in the middle of a large grass field")
        time.sleep(4)
        print("You realize all your posessions are gone as you listen to the wind whistle through the grass.")
        time.sleep(3)
        print("\n\nfarewell, brave adventurer")
    f = open("Title_Card.txt")
    lines = f.readlines()
    for i in range(len(lines)):
        content = lines[i].strip("\n")
        print(content)
        time.sleep(0.5)
    f.close
def warp_room(player1, door):
    if door == 1:
        item_room(player1)
    elif door == 2:
        monster_room(player1)
    elif door == 3:
        trap_room(player1)




def stats(player1):
    print(f"Name = {player1.name}")
    print(f"Level = {player1.LVL}")
    print(f"Health = {player1.HP} hp")
    print(f"Strength (total) = {player1.STR + player1.eqipped.strength} str")
    print(f"Body = {player1.STR} STR")
    print(f"Weapon = {player1.eqipped.strength} STR")


#A bunch of generation stuff down here (and some other small functions)


def door_ascii():
    door_content = open("door.txt")
    door = door_content.read()
    print(door)
    door_content.close()
    return


intro()