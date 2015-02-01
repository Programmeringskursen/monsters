import math
import numpy as np
FULL_LIFE = 10
MAX_MONSTER_STRENGTH = 5

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

class Player(Character):
    def __init__(self, position, life):
        Character.__init__(self, position)
        self.life = int(life)

    def fight(self, monster):
        if self.life < monster.strength and np.random.random()/0.5>1.:
            self.life -= 1
            print "You are defeated by the monster in the room! life -1"
        else:
            monster.place(None)

    def navigate(self):
        print "You are in room %d!"%(self.position) #This is really NOT the room ID yet!

class Monster(Character):
    def __init__(self, position, strength):
        Character.__init__(self, position)
        self.strength = int(strength)

class Room(object):
    def __init__(self, ID):
        self.ID = ID
        self.north = None
        self.south = None
        self.west = None
        self.east = None
        self.who = []

# set two rooms *self*, and *other* as neighbors
    def neighbor(self, other, direction):
        if direction == "north":
            self.north = other
            other.south = self
        elif direction == "south":
            self.south = other
            other.north = self
        if direction == "west":
            self.west = other
            other.east = self
        if direction == "east":
            self.east = other
            other.west = self

    def __repr__(self):
        return 'Room ID: %d'%(self.ID)

    def encounter(self):
        players_in_room = [char_in_room for char_in_room in self.who if isinstance(char_in_room, Player)]
        if players_in_room:
            monsters_in_room = [char_in_room for char_in_room in self.who if isinstance(char_in_room, Monster)]
            for monster_to_fight in monsters_in_room:
                player.fight(monster_to_fight)

class Game(object):
    def __init__(self, board_edge_length, monster_nr):
        self.rooms = []
        for room in xrange(board_edge_length**2):
            self.rooms.append(Room(room))
        def room_index(i, j):
            return j*board_edge_length+i
        for room_i in xrange(board_edge_length):
            for room_j in xrange(board_edge_length):
                room = self.rooms[room_index(room_i, room_j)]
                if room_i == 0:
                    room.neighbor(self.rooms[room_index(board_edge_length-1, room_j)], "west")
                if room_i == board_edge_length-1:
                    room.neighbor(self.rooms[room_index(0, room_j)], "east")
                if room_j == 0:
                    room.neighbor(self.rooms[room_index(room_i, board_edge_length-1)], "south")
                if room_j == board_edge_length-1:
                    room.neighbor(self.rooms[room_index(room_i, 0)], "north")
                else: 
                    room.neighbor(self.rooms[room_index(room_i, room_j+1)], "north")
                    room.neighbor(self.rooms[room_index(room_i, room_j-1)], "south")
                    room.neighbor(self.rooms[room_index(room_i-1, room_j)], "west")
                    room.neighbor(self.rooms[room_index(room_i+1, room_j)], "east")
        player_position = np.random.random_integers(board_edge_length)
        self.player = Player(self.rooms[player_position], FULL_LIFE)
        self.monsters = []
        monster_positions = np.random.random_integers(board_edge_length**2, size=monster_nr)
        monster_strengths = np.random.random_integers(MAX_MONSTER_STRENGTH, size=monster_nr)
        for monster in xrange(monster_nr):
            self.monsters.append(Monster(self.rooms[monster_positions[monster]], monster_strengths[monster]))

# draw the board
        i = 0
        for room in self.rooms:
            i += 1
            if room == self.player.position:
                print 'P\t'
            j = 0
            for j in range(monster_nr):
                if room == self.monsters[j].position:
                    print 'M%d\t'%(j)
            else:
                print 'X\t'
            if i%board_edge_length==0:
                print '\n'
            

g1 = Game(4, 2)
#                if room_i == 0:
#                    room.neighbor(self.rooms[room_i+board_edge_length, room_j], "west")
#                if room_i == board_edge_length-1:
#                    room.neighbor(self.rooms[0, room_j], "east")
#                if room_j == 0:
#                    room.neighbor(self.rooms[room_i, room_j+board_edge_length], "south")
#                if room_j == board_edge_length-1:
#                    room.neighbor(self.rooms[room_i, 0], "north")
#                else: 
#                    room.neighbor(self.rooms[room_index(room_i, room_j+1)], "north")
#                    room.neighbor(self.rooms[room_i, room_j-1], "south")
#                    room.neighbor(self.rooms[room_i-1, room_j], "west")
#                    room.neighbor(self.rooms[room_i+1, room_j], "east")
