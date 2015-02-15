import math
import numpy as np
import sys
import koffolsmonsters.exceptions

class Character(object):
    def __init__(self, position):
        self.position = None
        self.place(position)
        self.content = []

# puts the character *self* in the given *position*
    def place(self, position):
        if self.position != None:
            self.position.content.remove(self)
        self.position = position
        if position != None:
            position.content.append(self)

# moves the character *self* to its given *direction*
    def move(self, direction):
        if direction == "south":
            self.place(self.position.north)
        elif direction == "north":
            self.place(self.position.south)
        elif direction == "west":
            self.place(self.position.west)
        elif direction == "east":
            self.place(self.position.east)
        else:
            raise koffolsmonsters.exceptions.DirectionException()


