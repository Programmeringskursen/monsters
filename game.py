import math
import numpy as np
FULL_LIFE = 10
MAX_MONSTER_STRENGTH = 5
import sys

class DirectionException(Exception):
    pass

try:
    raise DirectionException("You can only go east, west, north, or south!")
except DirectionException, e:
    print e

    def direction_exception(direction):
        if direction != 'east' and direction != 'east' and direction != 'east' and direction != 'east':
            raise DirectionException("You can only go east, west, north, or south!")

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
    def __init__(self, board_edge_length=5, monster_nr=3):
        self.board_edge_length = board_edge_length
        self.monster_nr = monster_nr
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
        monster_positions = np.random.random_integers(0, board_edge_length**2-1, size=monster_nr)
        monster_strengths = np.random.random_integers(0, MAX_MONSTER_STRENGTH, size=monster_nr)
        for monster in xrange(monster_nr):
            self.monsters.append(Monster(self.rooms[monster_positions[monster]], monster_strengths[monster]))
        self.draw()
        self.play()
        self.draw()

# play one step
    def play(self):
        input_command = raw_input('How do you want to explore the world?\n')
        usr_commands = input_command.split()
        for cmnd in usr_commands:

            try: 
                self.direction = cmnd
                self.player.move(self.direction)
            except DirectionException

#        for room in self.rooms:
#            room.encounter()

# draw the board
    def draw(self):
            i = 0
            for room in self.rooms:
                i += 1
                if len(room.who) == 0:
                    sys.stdout.write('X\t')
                else:
                    for j in xrange(len(room.who)):
                        if room.who[j] == self.player:
                            sys.stdout.write('P')
                        else:
                            for k in xrange(self.monster_nr):
                                if room.who[j] == self.monsters[k]:
                                    sys.stdout.write('M%d'%(k))
                    sys.stdout.write('\t')
                if i%self.board_edge_length==0:
                    sys.stdout.write('\n')
            sys.stdout.flush()

print '\n'
g2 = Game()
