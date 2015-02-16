import math
import numpy as np
import sys
import koffolsmonsters.exceptions
import koffolsmonsters.player as player
import koffolsmonsters.monsters as monsters
import koffolsmonsters.things as things

class Room(object):
    def __init__(self, ID, game):
        self.ID = ID
        self.north = None
        self.south = None
        self.west = None
        self.east = None
        self.content = []
        self.game = game

    def __repr__(self):
        return 'Room ID: %d'%(self.ID)

# set two rooms *self*, and *other* as neighbors
    def neighbor(self, other, direction):
        if direction == "south":
            self.north = other
            other.south = self
        elif direction == "north":
            self.south = other
            other.north = self
        elif direction == "west":
            self.west = other
            other.east = self
        elif direction == "east":
            self.east = other
            other.west = self
        else:
            raise koffolsmonsters.exceptions.DirectionException()

    def encounter(self):
        players_in_room = [char_in_room for char_in_room in self.content if isinstance(char_in_room, player.Player)]
        if players_in_room:
            monsters_in_room = [char_in_room for char_in_room in self.content if isinstance(char_in_room, monsters.Monster)]
            for monster_to_fight in monsters_in_room:
                players_in_room[0].fight(monster_to_fight)


