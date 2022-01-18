import time
import random as rand
from Classes import Monster
from pain import pain_room
def monster_room(player1):
    monster_type = ["slime","Ingvar Kamprad","dragon","troll","skeleton","demon","golem","U̴̩̺̭͕̱̤͌̀͂ͅñ̸̺͕̃̄k̷̡̲̩̜̜͍͎̖̟͊ņ̴̨̡͕̲̭̮̝̣̌̈́͐̒̑͠o̶̡̦͙̯̭̭̥̪̲͋̊̐͐̿̄͛͜͝ŵ̷̛̛̗̞̘̱̞̃̈͗̕͘ͅn̵̝̳͚̹̈̿̓̈́ ̵̭̬͙̱͚́̑E̷̙̖͇̤͚̜̮̺͎͂̀́ṇ̵̟͔͠t̶̡̯̤̲͕͙̖̝̐͒͑̈͛͆͂̎̚i̴͖̻͎͕͔̼͚̬̒̔͊̓͛̓̈́t̴̬̠͕̼̭̾ͅẙ̶̫̱̮̃͗̈́̅̆̕͜͝"] #List of all monster types
    #The strength_index determines weater the player will encounter a weaker or a stronger monster.
    strength_index = rand.randint(1,6)
    if strength_index > 5:
        enemy_str = player1.STR + rand.randint(-2,3)
    else:
        enemy_str = player1.STR + rand.randint(-1,6)
    #Finnaly, the enemy is created by selecting a random monster type + giving it the strength previosuly generated
    enemy = Monster(monster_type[rand.randint(0,7)],enemy_str) 
    battle_room(player1,enemy)
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

#This if code will randomly decide if you win or loose based on the odds of winning (previously generated with relative STR)
#The code will open one out of two documents depending on the outcome of the battle. (Loosing stories or winning stories)
    while True:
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

    #Depending on the monster, we select wich story to read. We do not need to account for
    #loss or victory since the stories are the same legnth in both the winn and lose document (one of which was opened earlier)
            lines = f.readlines() 
            if monster.type == "slime":
                story_start = 0 #The first line of the story
                story_duration = 3 #The duration (ammount of lines) in the story
            elif monster.type == "dragon":
                story_start = 4
                story_duration = 7
            elif monster.type == "demon":
                story_start = 12
                story_duration = 5
            elif monster.type == "golem":
                story_start = 18
                story_duration = 6
            elif monster.type == "Mimic":
                story_start =25
                story_duration = 4
            elif monster.type == "Invar Kamprad":
                story_start = 30
                story_duration = 5
            elif monster.type == "troll":
                story_start = 36
                story_duration = 4
            elif monster.type == "skeleton":
                story_start = 41
                story_duration = 7
            else:
                print("ERROR")
                story_start = 49
                story_duration = 4

            for i in range(story_duration):
                print(lines[story_start+i])
                time.sleep(3)
                f.close()

            if damage == "y":
                player1.eqipped.potion_boost = 0 #After a battle the weapons potion boost is "consumed" and defaults to 0
                pain_room(player1,2)
                return
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
            return


        else:
            print("Thats not an option! Pull yourself together you're in a battle!")
            time.sleep(1)

        