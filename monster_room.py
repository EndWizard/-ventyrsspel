import time
import random as rand
from Classes import Monster
from pain import pain_room
def monster_room(player1):
    if player1.LVL <=9:
        monster_type = ["slime","goblin","dragon","orc","troll","undead","elemental","fiend/demon/devil","golem"]
        enemy = Monster(monster_type[rand.randint(0,8)],rand.randint(1,10)) 
        battle_room(player1,enemy)
    else:
        boss_type = ["old gnawbone","achererach"]
        battle_room(player1,Monster[rand.randint(0,1)],15)
    return

def battle_room(player1, monster):
    print(f"A {monster.type} appears!")
    time.sleep(2)
    relative_str = monster.strength - (player1.STR + player1.eqipped.strength + player1.eqipped.potion_boost)
    #Uses relative_str to check chance of winning + message
    if relative_str < 0:            
        print("It looks rather weak")
        chance = "100%"
    elif relative_str <=2:
        print("It looks rather strong, but you might be able to take it...")
        chance = "40%"
    else:
        print("It looks very strong! Taking on this monster will be difficult.")
        chance = "10%"

    #Decide to run or fight
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
            story_start = 0
            story_duration = 3
        else:
            print("Under construction")
            story_start = 0
            story_duration = 3
        for i in range(story_duration):
            print(lines[story_start+i])
            time.sleep(3)
            f.close()
        #checks if player takes damage, and removes potion boosts
        if damage == "y":
            player1.eqipped.potion_boost = 0 
            pain_room(player1,2)
        else:
            player1.LVL = player1.LVL + 1
            player1.eqipped.potion_boost = 0 
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

    