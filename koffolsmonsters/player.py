import math
import numpy as np
import sys
import koffolsmonsters.characters as characters

class Player(characters.Character):
    def __init__(self, position, life):
        characters.Character.__init__(self, position)
        self.life = int(life)

# measures the player's remaining strength to that of the monste's in the same room
    def fight(self, monster):
        if self.life < monster.strength and np.random.random()*2.>1.:
            self.life -= 1
            if  self.life == 1:
                print "You are defeated by the monster in the room! Only 1 life left!"
            elif self.life >1:
                print "You are defeated by the monster in the room! %d lives left!" %(self.life)
            elif self.life == 0:
                print "You are defeated by the monster in the room and died FOREVER! Yoohahahaaa!"
        else:
            print "Monster %s is defeated! Yay!"%(monster.name)
            monster.position.game.monsters.remove(monster)
            monster.place(None)

# shows where the player is located
    def navigate(self):
        print "You are in room %d!"%(self.position) #This is really NOT the room ID yet!

    def __repr__(self):
        return "P"
