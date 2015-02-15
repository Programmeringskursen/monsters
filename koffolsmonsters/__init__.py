import math
import numpy as np
FULL_LIFE = 2
MAX_MONSTER_STRENGTH = 5
import sys
import koffolsmonsters.exceptions
import koffolsmonsters.characters as characters
import koffolsmonsters.player as player
import koffolsmonsters.monsters as monsters
import koffolsmonsters.rooms as rooms

class Game(object):
    def __init__(self, board_edge_length=5, monster_nr=3):
        self.board_edge_length = board_edge_length
        self.monster_nr = monster_nr
        self.rooms = []
        for room in xrange(board_edge_length**2):
            self.rooms.append(rooms.Room(room, self))
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
                    room.neighbor(self.rooms[room_index(room_i, board_edge_length-1)], "north")
                if room_j == board_edge_length-1:
                    room.neighbor(self.rooms[room_index(room_i, 0)], "south")
                else: 
                    room.neighbor(self.rooms[room_index(room_i, room_j+1)], "south")
                    room.neighbor(self.rooms[room_index(room_i, room_j-1)], "north")
                    room.neighbor(self.rooms[room_index(room_i-1, room_j)], "west")
                    room.neighbor(self.rooms[room_index(room_i+1, room_j)], "east")
        player_position = np.random.random_integers(board_edge_length)
        self.player = player.Player(self.rooms[player_position], FULL_LIFE)
        self.monsters = []
        monster_positions = np.random.random_integers(0, board_edge_length**2-1, size=monster_nr)
        monster_strengths = np.random.random_integers(0, MAX_MONSTER_STRENGTH, size=monster_nr)
        for monster in xrange(monster_nr):
            self.monsters.append(monsters.Monster(self.rooms[monster_positions[monster]], monster_strengths[monster], '%s'%(monster,)))
            self.check_encounters()
        while self.player.life and self.monsters:
            self.draw()
            self.play()
            self.check_encounters()
        else:
            print "This fight is not over!!"

# Encountering
    def check_encounters(self):
        for room in self.rooms:
            room.encounter()


# play one step
    def play(self):
        cmnd_validity = False
        while cmnd_validity == False:
            input_command = raw_input('How do you want to explore the world?\n')
            usr_commands = input_command.split()
            for cmnd in usr_commands:
                try:
                    self.direction = cmnd
                    self.player.move(self.direction)
                    cmnd_validity = True
                except koffolsmonsters.exceptions.DirectionException, e:
                    cmnd_validity = False

# draw the board
    def draw(self):
            i = 0
            for room in self.rooms:
                i += 1
                if len(room.who) == 0:
                    sys.stdout.write('X\t')
                else:
                    for character in room.who:
                        sys.stdout.write(repr(character))
                    sys.stdout.write('\t')
                if i%self.board_edge_length==0:
                    sys.stdout.write('\n')
            sys.stdout.flush()

print '\n'

