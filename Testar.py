import time
class Weapon():
    def __init__(self, item, strength, lore):
        self.item = item
        self.strength = strength


class Player():
    def __init__(self, hp, STR):
        self.hp = hp
        self.eqipped = 0
        self.STR = STR 
        self.lvl = 0
        self.inv = [] 

sword = Weapon("rusty shortsword",3, "a extremly old sword made of copper")
test = Player(10, 3)
test.inv.append(sword)
test.inv.append(Weapon("torch", 0, "a glowing object"))
test.eqipped = sword

def backpack():
    while True:
        print ("\n~~~~backpack~~~~\n")
        x=1
        for i in test.inv:
            print (f"|{x} {i.item}")
            x=x+1
        menu=input("(r) Return,(d) Discard,(i) Inspect,(e) Equip,(u)Use -> ")
        if menu in {"r","R","d","D","i","I","e","E","u","U"}:
            if menu in {"r","R"}:
                break
            if menu in {"d","D"}:
                choice = input(f"Choose item to discard (1-{len(test.inv)}) -> ")
                if choice.isdigit():
                    choice = int(choice)
                    if (1 <= choice <= len(test.inv)):
                        warning = input(f"Are you sure you whant to discard {test.inv[choice-1].item} [y/n] -> ")
                        if warning in {"y","Y","n","N"}:
                            if warning in {"y","Y"}:
                                print(f"You trow away your {test.inv[choice-1].item}")
                                test.inv.pop(choice-1)
                            if warning in {"n","N"}:
                                print(f"You deside to not throw away your {test.inv[choice-1].item}")
                            else:
                                print("wrong")
                        else:
                            print("wrong")
                    else:
                        print("wrong")
                else:
                    print("wrong")
            if menu in {"i","I"}:
                choice = input(f"Choose item to inspect (1-{len(test.inv)}) -> ")
                if choice.isdigit():
                    choice = int(choice)
                    if (1 <= choice <= len(test.inv)):
                        print(f"\n{test.inv[choice-1].item}")
                        print(test.inv[choice-1].strength)
                        input("\npress enter to continue")
                    else:
                        print("wrong")
                else:
                    print("wrong")
            if menu in {"e","E"}:
                choice = input(f"Choose item to equip (1-{len(test.inv)}) -> ")
                if choice.isdigit():
                    choice = int(choice)
                    if (1 <= choice <= len(test.inv)):
                        warning = input(f"Are you sure you whant to change your {test.eqipped.item} that has a strength of {test.eqipped.strength} to your {test.inv[choice-1].item} that has a strength of {test.inv[choice-1].strength}? \n[y/n]-> ")
                        if warning in {"y","Y"}:
                            test.eqipped = test.inv[choice-1]
                            print(f"You are now using {test.eqipped.item}")
                        if warning in {"n","N"}:
                            print(f"You keep your {test.eqipped.item} equipped")
                else:
                    print ("wrong")
            if menu in {"u","U"}:
                choice = input(f"Choose item to use (1-{len(test.inv)}) -> ")
                if choice.isdigit():
                    choice = int(choice)
                    if (1 <= choice <= len(test.inv)):
                        print("hello")
        else :
            print("Felaktigt val")

backpack()