import math
import numpy as np
FULL_LIFE = 10
MAX_MONSTER_STRENGTH = 5
import sys
import characters

class Player(characters.Character):
    def __init__(self, position, life):
        characters.Character.__init__(self, position)
        self.life = int(life)

# measures the player's remaining strength to that of the monste's in the same room
    def fight(self, monster):
        if self.life < monster.strength and np.random.random()*2.>1.:
            self.life -= 1
            print "You are defeated by the monster in the room! life -1"
        else:
            monster.place(None)

# shows where the player is located
    def navigate(self):
        print "You are in room %d!"%(self.position) #This is really NOT the room ID yet!

