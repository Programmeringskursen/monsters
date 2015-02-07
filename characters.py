import math
import numpy as np
import sys
import exceptions

class Character(object):
    def __init__(self, position):
        self.position = None
        self.place(position)

# puts the character *self* in the given *position*
    def place(self, position):
        if self.position != None:
            self.position.who.remove(self)
        self.position = position
        if position != None:
            position.who.append(self)

# moves the character *self* to its given *direction*
    def move(self, direction):
        if direction == "north":
            self.place(self.position.north)
        elif direction == "south":
            self.place(self.position.south)
        elif direction == "west":
            self.place(self.position.west)
        elif direction == "east":
            self.place(self.position.east)
        else:
            raise exceptions.DirectionException()


