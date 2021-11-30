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

class Player():
    def __init__(self, name):
        self.HP = 10
        self.STR = 3
        self.LVL = 0
        self.eqipped = 0
        self.inv = []
        self.name = name

name = input("\n\nWhat is your name travler? :")
rusty_sword = Weapon("Rusty Shortsword","It's a rusty old sword you found on the ground...",1)
player1 = Player(name)
player1.eqipped = rusty_sword
player1.inv.append(Item("torch","Its dark to go alone, take this!"))
player1.inv.append(rusty_sword)

def backpack(player1):
    while True:
        print ("\n~~~~backpack~~~~\n")
        x=1
        for i in player1.inv:
            print (f"|{x} {i.item}")
            x=x+1
        menu=input("(r) Return,(d) Discard,(i) Inspect,(e) Equip,(u)Use -> ")
        menu=menu.lower()
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
                                warning = input(f"Are you sure you whant to discard {player1.inv[choice-1].item} [y/n] -> ")
                                if warning in {"y","Y"}:
                                    print(f"You trow away your {player1.inv[choice-1].item}")
                                    player1.inv.pop(choice-1)
                                    break
                                elif warning in {"n","N"}:
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
        elif menu in {"e","E"}:
            while True:
                choice = input(f"Choose item to equip (1-{len(player1.inv)}) -> ")
                if choice.isdigit():
                    choice = int(choice)
                    if (1 <= choice <= len(player1.inv)):
                        if player1.inv[choice-1].type == "weapon":
                            while True:
                                warning = input(f"Are you sure you whant to change your {player1.eqipped.item} that has a strength of {player1.eqipped.strength} to your {player1.inv[choice-1].item} that has a strength of {player1.inv[choice-1].strength}? \n[y/n]-> ")
                                if warning in {"y","Y"}:
                                    player1.eqipped = player1.inv[choice-1]
                                    print(f"You are now using {player1.eqipped.item}")
                                    break
                                elif warning in {"n","N"}:
                                    print(f"You keep your {player1.eqipped.item} equipped")
                                    break           
                        else:
                            print("you can't equip that")
                        break

        elif menu in {"u","U"}:
            print("under construction")
            """choice = input(f"Choose item to use (1-{len(player1.inv)}) -> ")
            if choice.isdigit():
                choice = int(choice)
                if (1 <= choice <= len(player1.inv)):
                    print("hello")"""



backpack(player1)