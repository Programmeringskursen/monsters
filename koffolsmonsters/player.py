import math
import numpy as np
import sys
import koffolsmonsters.characters as characters
import koffolsmonsters.exceptions

class Player(characters.Character):
    def __init__(self, position, life):
        characters.Character.__init__(self, position)
        self.life = int(life)

    def __repr__(self):
        return "*"

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

    def pickup(self, thing):
        print "Pick up %s!"%(thing)
#        for item in self.position.content:
#            if repr(item)!=thing: continue  
#            item.place(self.position)
        matching_thing = [item for item in self.position.content if repr(item)==thing]
        if matching_thing:
            matching_thing[0].place(self.position)
            print "%s is now in your backpack!"%(thing)
        elif not thing in [repr(item) for item in self.position.game.things_in_game]:
            raise koffolsmonsters.exceptions.ThingNameException()
