import time
import random as rand
from Classes import Monster
from pain import pain_room
def monster_room(player1):
    if player1.LVL <=9: #Depending on the players level, this if code might give you a "boss battle"
        monster_type = ["slime","goblin","dragon","troll","undead","demon","golem"] #List of all monster types
        #The strength_index determines weater the player will encounter a weaker or a stronger monster.
        strength_index = rand.randint(1,6)
        if strength_index > 5:
            enemy_str = player1.STR + rand.randint(-2,3)
        else:
            enemy_str = player1.STR + rand.randint(-1,6)
        #Finnaly, the enemy is created by selecting a random monster type + giving it the strength previosuly generated
        enemy = Monster(monster_type[rand.randint(0,8)],enemy_str) 
        battle_room(player1,enemy)
    else: 
        boss_type = ["old gnawbone","achererach","ingvar kamprad"]
        battle_room(player1,Monster[rand.randint(0,1)],15)
    return

def battle_room(player1, monster):
    print(f"A {monster.type} appears!")
    time.sleep(2)
        #Uses relative_str to check chance of winning
    relative_str = monster.strength - (player1.STR + player1.eqipped.strength + player1.eqipped.potion_boost)
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
    #The following if code will randomize the outcome of the battle. Win = Open the document with winning stories
    #lose = open document with losing stories
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
#"story checklist"
#dragon DONE
#demon DONE
#slime DONE
#goblin
#troll
#undead
#golem DONE
        lines = f.readlines() #After the If code opens one of the two documents, the program reads it
        if monster.type == "slime": #
            story_start = 0
            story_duration = 3
        elif monster.type == "dragon":
            story_start = 4
            story_duration = 7
        elif monster.type == "demon":
            story_start = 12
            story_duration = 5
        elif monster.type == "golem":
            story_start = 18
            story_duration = 6
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

    