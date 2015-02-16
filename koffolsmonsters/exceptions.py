import math
import numpy as np
import sys

class DirectionException(Exception):
    def __init__(self):
        Exception.__init__(self, "Invalid direction keyword; Try with east, west, north or south")

class ThingNameException(Exception):
    def __init__(self):
        Exception.__init__(self, "Invalid thing!")

