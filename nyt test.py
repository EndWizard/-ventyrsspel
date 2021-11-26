import random as rand
f = open('Weapons.txt')
lines = f.readlines()
while True:
    type = rand.randint(1,8)
    weapon_type = ((type*2)-1)
    print(type, weapon_type)
    print(lines[weapon_type], lines[weapon_type+1])
    input()
