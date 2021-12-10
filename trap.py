import time
import random as rand
from pain import pain_room

def trap_room(player1):
    f = open("Traps.txt")
    lines = f.readlines()
    random = rand.randint(1,7)

    if random == 1:
        story_start = 0
        story_duration = 14
    elif random == 2:
        story_start = 15
        story_duration = 15
    elif random == 3:
        story_start = 31
        story_duration = 15
    elif random == 4:
        story_start = 47
        story_duration = 10
    elif random == 5:
        story_start = 58
        story_duration = 10
    elif random == 6:
        story_start = 69
        story_duration = 15
    elif random == 7:
        story_start = 85
        story_duration = 11

    for i in range(story_duration):
        print(lines[story_start+i])
        time.sleep(3)
    f.close()
    pain_room(player1,1)