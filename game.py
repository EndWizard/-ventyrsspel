import random as rand
import time

class Weapon():
    def __init__(self, item, desc, strength):
        self.item = item
        self.strength = strength
        self.type = "weapon"
        self.desc = desc

class Item():
    def __init__(self, item, description):
        self.item = item
        self.type = "item"
        self.description = description
        
class Junk():
    def __init__(self, item):
        self.item = item
        self.type = "junk"
        self.description = "This item is useless... Why do you hold on to it?"

class Monster():
    def __init__(self, type, str):
        self.type = type
        self.strength = str



class Player():
    def __init__(self, name):
        self.HP = 10
        self.STR = 3
        self.LVL = 0
        self.eqipped = 0
        self.inv = []
        self.name = name



def pain_room(player1, ammount):
    player1.HP = player1.HP - ammount
    return

def intro():
    title = input("Skip title screen? [y/n] :").casefold()
    if title == "n":
        f = open("Title_card.txt")
        lines = f.readlines()
        for i in range(len(lines)):
            content = lines[i].strip("\n")
            print(content)
            time.sleep(0.5)
    elif title == "y":
        print("")
    else:
        print("")

    name = input("\n\nWhat is your name travler? :")
    rusty_sword = Weapon("Rusty Shortsword","It's a rusty old sword you found on the ground...",1)
    player1 = Player(name)
    player1.eqipped = rusty_sword
    player1.inv.append(Item("torch","Its dark to go alone, take this!"))
    player1.inv.append(rusty_sword)
    time.sleep(1)
    print("\nYou find yourself in a dark room.")
    time.sleep(1)
    print("A flickering torch is sitting on the wall, you grab it\n")
    time.sleep(1)
    main_room(player1)

def main_room(player1):
    if player1.HP > 1:
        door1 = 2 #rand.randint(1,3)
        door2 = rand.randint(1,3)
        door3 = rand.randint(1,3)
    else:
        door1 = rand.randint(1,2)
        door2 = rand.randint(1,2)
        door3 = rand.randint(1,2)

    
    while player1.HP >= 1:
    
        print("\n~~~Dungeon room(or something more creative later on)~~~\n\n1 Explore [E]    2 Check stats [S]\n3 Check backpack [B]")
        goto = input("\nSelect menu option :").lower()
        if goto == "e":
            time.sleep(1)
            print("\n you approach three doors.")
            time.sleep(1)
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
            elif door == "1": #test för item room ska tas bort när vi är klara
                warp_room(player1,1)
        if goto == "b":
            backpack(player1)
        if goto == "s":
            stats(player1)
    print("lol u dieded")


def warp_room(player1, door):
    if door == 1:
        item_room(player1)
    elif door == 2:
        monster_room(player1)
    elif door == 3:
        trap_room(player1)

def backpack(player1):
    while True:
        print ("\n~~~~backpack~~~~\n")
        x=1
        for i in player1.inv:
            print (f"|{x} {i.item}")
            x=x+1
        menu=input("(r) Return,(d) Discard,(i) Inspect,(e) Equip,(u)Use -> ").lower()
        if menu in {"r"}:
            break
        elif menu in {"d"}:
            while True:
                choice = input(f"Choose item to discard (1-{len(player1.inv)}) -> ")
                if choice.isdigit():
                    choice = int(choice)
                    if (1 <= choice <= len(player1.inv)):
                        if player1.inv[choice-1] == player1.eqipped:
                            print("You can't discard equipped weapons")
                            break
                        else:
                            while True:
                                warning = input(f"Are you sure you whant to discard {player1.inv[choice-1].item} [y/n] -> ").lower()
                                if warning in {"y"}:
                                    print(f"You trow away your {player1.inv[choice-1].item}")
                                    player1.inv.pop(choice-1)
                                    break
                                elif warning in {"n"}:
                                    print(f"You deside to not throw away your {player1.inv[choice-1].item}")
                                    break
                            break         
        elif menu in {"i"}:
            while True:
                choice = input(f"Choose item to inspect (1-{len(player1.inv)}) -> ")
                if choice.isdigit():
                    choice = int(choice)
                    if (1 <= choice <= len(player1.inv)):
                        if player1.inv[choice-1].type == "weapon":
                            print(f"\n{player1.inv[choice-1].item}")
                            print(f"{player1.inv[choice-1].desc}")
                            print(f"+{player1.inv[choice-1].strength} strength")
                            input("\npress enter to continue")
                        else:
                            print(f"\n{player1.inv[choice-1].item}")
                            print(player1.inv[choice-1].description)
                            input("\npress enter to continue")
                        break
        elif menu in {"e"}:
            while True:
                choice = input(f"Choose item to equip (1-{len(player1.inv)}) -> ")
                if choice.isdigit():
                    choice = int(choice)
                    if (1 <= choice <= len(player1.inv)):
                        if player1.inv[choice-1].type == "weapon":
                            while True:
                                warning = input(f"Are you sure you whant to change your {player1.eqipped.item} that has a strength of {player1.eqipped.strength} to your {player1.inv[choice-1].item} that has a strength of {player1.inv[choice-1].strength}? \n[y/n]-> ").lower()
                                if warning in {"y"}:
                                    player1.eqipped = player1.inv[choice-1]
                                    print(f"You are now using {player1.eqipped.item}")
                                    break
                                elif warning in {"n"}:
                                    print(f"You keep your {player1.eqipped.item} equipped")
                                    break           
                        else:
                            print("you can't equip that")
                        break

        elif menu in {"u"}:
            print("under construction")
            """choice = input(f"Choose item to use (1-{len(player1.inv)}) -> ")
            if choice.isdigit():
                choice = int(choice)
                if (1 <= choice <= len(player1.inv)):
                    print("hello")"""


def monster_room(player1):
    monster_type = ["slime","goblin","dragon","orc","troll","undead","elemental","fiend/demon/devil","golem"]
    enemy = Monster(monster_type[rand.randint(0,8)],rand.randint(1,10)) 
    battle_room(player1,enemy)
    return
    
def item_room(player1):
    print("Interesting story goes here, you find a chest or smth")
    mimic = rand.randint(1,10)
    if mimic == 10: #checks if the chest is a mimic
        print("mimic stuff")

    else: 
        item_type = rand.randint(1,10) 
        if item_type < 6:
            content = generate_weapon()
            loot_check(player1,content)
        elif 5 < item_type < 9:
            content = generate_weapon()
            """content = generate_item()"""
            loot_check(player1,content)
        elif 8 < item_type:
            content = generate_junk()
            loot_check(player1,content)



def trap_room(player1):
    f = open("Traps.txt")
    lines = f.readlines()
    random = rand.randint(1,7)

    if random == 1:
        story_start = 0
        story_duration = 14
    elif random == 2:
        story_start = 15
        story_duration = 15
    elif random == 3:
        story_start = 31
        story_duration = 15
    elif random == 4:
        story_start = 47
        story_duration = 10
    elif random == 5:
        story_start = 58
        story_duration = 10
    elif random == 6:
        story_start = 69
        story_duration = 15
    elif random == 7:
        story_start = 85
        story_duration = 11

    for i in range(story_duration):
        print(lines[story_start+i])
        time.sleep(3)
    f.close()
    pain_room(player1,1)
    
def battle_room(player1, monster):
    print(f"A {monster.type} appears!")
    time.sleep(2)
    relative_str = monster.strength - (player1.STR + player1.eqipped.strength)
    if relative_str < 0:            
        print("It looks rather weak")
        chance = "100%"
    elif relative_str <=2:
        print("It looks rather strong, but you might be able to take it...")
        chance = "40%"
    else:
        print("It looks very strong! Taking on this monster will be difficult.")
        chance = "10%"
    time.sleep(2)
    print("\nWhat do you want to do?")
    print(f"\n[f]Fight[{chance} success]")
    print(f"[r]Run![-1 HP]")
    fight = input(f"\nChoose :").lower()
    if fight == "fight" or fight == "f":
        if chance == "100%":
            f = open("MonsterWin.txt")
            damage = "n"
        elif chance == "40%":
            win = rand.randint(1,5)
            if win > 3:
                f = open("MonsterWin.txt")
                damage ="n"
            else:
                f = open("MonsterDmg.txt")
                damage = "y"
        elif chance == "10%":
            win = rand.randint(1,10)
            if win == 4:
                f = open("MonsterWin.txt")
                damage ="n"
            else:
                f = open("MonsterDmg.txt")
                damage ="y"

        lines = f.readlines()
        if monster.type == "slime":
            story_start = 0
            story_duration = 3
        elif monster.type == "dragon":
            print("under construction")
        else:
            print("Under construction")
        for i in range(story_duration):
            print(lines[story_start+i])
            time.sleep(3)
            f.close()
        if damage == "y":
            pain_room(player1,2)
        else:
            return
    elif fight == "run" or fight == "r": 
        print("\nYou don't risk it, and instead you make a dash for the door.")
        time.sleep(2)
        print("However, while dashing for the exit you trip on a rock")
        time.sleep(1)
        print("You scrape your knee")
        time.sleep(1)
        print("-1HP")
        pain_room(player1,1)



def stats(player1):
    print(f"Name = {player1.name}")
    print(f"Level = {player1.LVL}")
    print(f"Health = {player1.HP} hp")
    print(f"Strength (total) = {player1.STR + player1.eqipped.strength} str")
    print(f"Body = {player1.STR} STR")
    print(f"Weapon = {player1.eqipped.strength} STR")


def door_ascii():
    door_content = open("door.txt")
    door = door_content.read()
    print(door)
    door_content.close()
    return



def generate_item():
    print("nope")

def generate_weapon():
    f = open('Weapons.txt')
    lines = f.readlines()
    type = rand.randint(1,8)
    weapon_type = ((type*2)-1)
    chest_content = Weapon(lines[weapon_type].strip("\n"), lines[weapon_type+1].strip("\n"),1)
    print(f"You open the chest to discover a {chest_content.item} with a strength of {chest_content.strength}")
    return chest_content


def generate_junk():
    junk_list = ["stick", "broken bottle", "tin can"]
    chest_content = Junk(junk_list[rand.randint(0,2)])
    print(f"You open the chest to discover a {chest_content.item}")
    return chest_content

def loot_check(player1,content):
    if len(player1.inv) <= 4:
        player1.inv.append(content)
    else :
        while True:
            anser = input(f"your inventory is full, do you whant to discard an item to pick up {content.item} [y/n] -> ").lower()
            if anser in {"y"}:
                x=1
                for i in player1.inv:
                    print (f"|{x} {i.item}")
                    x=x+1
                choice = input(f"Choose item to discard (1-{len(player1.inv)}) -> ")
                if choice.isdigit():
                    choice = int(choice)
                    if (1 <= choice <= len(player1.inv)):
                        if player1.inv[choice-1] == player1.eqipped:
                            print("You can't discard equipped weapons")
                        else:
                            warning = input(f"Are you sure you whant to discard {player1.inv[choice-1].item} for {content.item} [y/n] -> ").lower()
                            if warning in {"y"}:
                                print(f"You trow away your {player1.inv[choice-1].item} and pick upp the {content.item}")
                                player1.inv.pop(choice-1)
                                player1.inv.append(content)
                                break
                            elif warning in {"n"}:
                                print(f"You deside to not throw away your {player1.inv[choice-1].item}")
            if anser in {"n"}:
                print(f"you leave the {content.item} behind")
                break

intro()