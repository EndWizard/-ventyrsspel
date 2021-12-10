import time
def backpack(player1):
    while True:
        print ("\n~~~~backpack~~~~\n")
        x=1
        for i in player1.inv:
            print (f"|{x} {i.item}")
            x=x+1
        menu=input("(r) Return,(t) Throw away,(i) Inspect,(e) Equip,(d)drink -> ").lower()
        if menu in {"r"}:
            break
        elif menu in {"t"}:
            while True:
                choice = input(f"Choose item to throw away (1-{len(player1.inv)}) -> ")
                if choice.isdigit():
                    choice = int(choice)
                    if (1 <= choice <= len(player1.inv)):
                        if player1.inv[choice-1] == player1.eqipped:
                            print("You can't throw away equipped weapons")
                            break
                        else:
                            while True:
                                warning = input(f"Are you sure you whant to throw away your {player1.inv[choice-1].item} [y/n] -> ").lower()
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
            while True:
                choice = input(f"Choose item to drink (1-{len(player1.inv)}) -> ")
                if choice.isdigit():
                    choice = int(choice)
                    if (1 <= choice <= len(player1.inv)):
                        if player1.inv[choice-1].type == "potion":
                            while True:
                                warning = input(f"Are you sure you whant to drink your {player1.inv[choice-1].item}? \n[y/n]-> ").lower()
                                if warning in {"y"}:
                                    print(f"You deside to drink your {player1.inv[choice-1].item}")
                                    if player1.inv[choice-1].item == "Potion of Healing":
                                        print("+1 HP")
                                        player1.HP = player1.HP + 1
                                        player1.inv.pop(choice-1)
                                        break
                                    elif player1.inv[choice-1].item == "Potion of Poison":
                                        print("why did you drink this\n -2 HP")
                                        player1.HP = player1.HP - 2
                                        player1.inv.pop(choice-1)
                                        break
                                    else:
                                        print("unkown potion")
                                        break
                                        
                                elif warning in {"n"}:
                                    print(f"You don't drink your {player1.inv[choice-1].item}")
                                    break           
                        else:
                            print("you can't drink that dummy")
                        break
