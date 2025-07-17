import math, pygame
from settings import *
from ray import Ray

class Raycaster:
    def __init__(self, player):
        self.rays = []
