class Monster():
    def __init__(self, type, str):
        self.type = type
        self.strength = str

class Weapon():
    def __init__(self, item, desc, strength):
        self.item = item
        self.strength = strength
        self.type = "weapon"
        self.desc = desc
        self.potion_boost = 0

class Potion():
    def __init__(self, item, description):
        self.item = item
        self.type = "potion"
        self.description = description
        
class Junk():
    def __init__(self, item):
        self.item = item
        self.type = "junk"
        self.description = "This item is useless... Why do you hold on to it?"


class Player():
    def __init__(self, name):
        self.HP = 10
        self.STR = 3
        self.LVL = 0
        self.eqipped = 0
        self.inv = []
        self.name = name
