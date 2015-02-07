import math
import numpy as np
FULL_LIFE = 10
MAX_MONSTER_STRENGTH = 5
import sys
import characters

class Monster(characters.Character):
    def __init__(self, position, strength):
        characters.Character.__init__(self, position)
        self.strength = int(strength)

