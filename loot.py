import time
import random as rand
from Classes import Monster, Potion, Weapon, Junk
from monster_room import battle_room

def item_room(player1):
    print("As you enter the room you see a large golden chest \n")
    time.sleep(1)
    mimic =rand.randint(1,10) #randomly generates a number to determine if the chest is a mimic
    save = player1.HP #Checks the players curren HP
    if mimic == 10: #checks if the chest is a mimic
        print("As you start opening the lid you see the endless rows of teeth within")
        time.sleep(1)
        battle_room(player1,Monster("Mimic",rand.randint(1,10))) #Sends the player to the battle room with a mimic
        
        
    #If the player returns from the mimic battle with the same HP, it means they won and recieve an item from the mimic
    #If the player never encountered a mimic, they will still recieve and item from a chest (since the only way they could lose HP is with a mimic).
    if save == player1.HP: 
        item_type = rand.randint(1,10) 
        if item_type < 6:
            content = generate_weapon()
            loot_check(player1,content)
        elif 5 < item_type < 9:
            content = generate_Potion()
            loot_check(player1,content)
        elif 8 < item_type:
            content = generate_junk()
            loot_check(player1,content)
    

def generate_Potion():
    f = open("Potions.txt")
    potions = f.readlines()
    potion_select = rand.randint(1,3) #and index used to select a potion
    potion_type = ((potion_select*2)-2) #Equation that uses the apropriate line from the text document
    potion = Potion(potions[potion_type].strip("\n"),potions[potion_type +1].strip("\n"))
    print(f"You open the chest and discover a {potion.item}")
    return potion

def generate_weapon():
    f = open('Weapons.txt')
    lines = f.readlines()
    type = rand.randint(1,8)
    weapon_type = ((type*2)-1)
    str_index = rand.randint(1,10)
    if str_index <= 6:
        weapon_str = rand.randint(1,3)
    elif str_index > 6:
        weapon_str = rand.randint(1,6)


    chest_content = Weapon(lines[weapon_type].strip("\n"), lines[weapon_type+1].strip("\n"),weapon_str)
    print(f"You open the chest and discover a {chest_content.item} with a strength of {chest_content.strength}")
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
            time.sleep(0.5)
            if anser in {"y"}:
                x=1
                for i in player1.inv:
                    print (f"|{x} {i.item}")
                    x=x+1
                choice = input(f"Choose item to discard (1-{len(player1.inv)}) -> ")
                time.sleep(0.5)
                if choice.isdigit():
                    choice = int(choice)
                    if (1 <= choice <= len(player1.inv)):
                        if player1.inv[choice-1] == player1.eqipped:
                            print("You can't discard equipped weapons")
                            time.sleep(0.5)
                        else:
                            warning = input(f"Are you sure you whant to discard {player1.inv[choice-1].item} for {content.item} [y/n] -> ").lower()
                            time.sleep(0.5)
                            if warning in {"y"}:
                                print(f"You trow away your {player1.inv[choice-1].item} and pick upp the {content.item}")
                                time.sleep(0.5)
                                player1.inv.pop(choice-1)
                                player1.inv.append(content)
                                break
                            elif warning in {"n"}:
                                print(f"You deside to not throw away your {player1.inv[choice-1].item}")
                                time.sleep(0.5)
            if anser in {"n"}:
                print(f"you leave the {content.item} behind")
                time.sleep(0.5)
                break