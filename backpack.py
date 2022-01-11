import time
def backpack(player1):
    while player1.HP >= 1 and player1.LVL <= 9 and player1.inv[0].type=="torch":
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
                                warning = input(f"Are you sure you whant to discard your {player1.inv[choice-1].item} [y/n] -> ").lower()
                                if warning in {"y"}:
                                    print(f"You discard your {player1.inv[choice-1].item}")
                                    player1.inv.pop(choice-1)
                                    break
                                elif warning in {"n"}:
                                    print(f"You deside to discard away your {player1.inv[choice-1].item}")
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
                elif choice in {"r","return"}:
                    break

        elif menu in {"u"}:
            while player1.HP >= 1 and player1.LVL <= 9 and player1.inv[0].type=="torch":
                use = input ("what do you whant to do? [d]Drink,[c]Coat weapon,[r]Return -> ").lower()
                if use in {"d"}:
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
                                            elif player1.inv[choice-1].item == "Potion of Seeing":
                                                print("The world seem to change around you") 
                                                player1.x_ray = True
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
                elif use in {"c"}:
                    while True:
                        choice = input (f"Choose item to coat your {player1.eqipped.item} with (1-{len(player1.inv)}) -> ")
                        if choice.isdigit():
                            choice = int(choice)
                            if (1 <= choice <= len(player1.inv)):
                                if player1.inv[choice-1].type == "potion":
                                    while True:
                                        warning = input(f"Are you sure you whant to coat your {player1.eqipped.item} with {player1.inv[choice-1].item}? \n[y/n]-> ").lower()
                                        if warning in {"y"}:
                                            print(f"You deside use a {player1.inv[choice-1].item} on your weapon")
                                            if player1.inv[choice-1].item == "Potion of Healing":
                                                print("That doesn't seem smart")
                                                player1.eqipped.potion_boost = -2
                                                player1.inv.pop(choice-1)
                                                break
                                            elif player1.inv[choice-1].item == "Potion of Poison":
                                                print("This will pack a punch")
                                                player1.eqipped.potion_boost = 2
                                                player1.inv.pop(choice-1)
                                                break
                                            elif player1.inv[choice-1].item == "Potion of Seeing":
                                                print("this doesn't SEEm to have an effect")
                                                player1.inv.pop(choice-1)
                                                break
                                            else:
                                                print("unkown potion")
                                                break
                                else:
                                    print("That's not a liquid... What are you trying to accomplish")
                                break
                elif use in {"r"}:
                    break