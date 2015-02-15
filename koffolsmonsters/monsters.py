import math
import numpy as np
import sys
import koffolsmonsters.characters as characters

class Monster(characters.Character):
    def __init__(self, position, strength, name):
        characters.Character.__init__(self, position)
        self.strength = int(strength)
        self.name = name

    def __repr__(self):
        return self.name

