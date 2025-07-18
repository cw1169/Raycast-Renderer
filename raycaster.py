import math, pygame
from settings import *
from ray import Ray

class Raycaster:
    def __init__(self, player, map):
        self.rays = []
        self.player = player
        self.map = map
    
    def castAllRays(self):
        self.rays = []
        rayAngle = (self.player.rotation_angle - FOV / 2)
        for i in range(num_rays):
            ray = Ray(rayAngle, self.player, self.map)
            ray.cast()
            self.rays.append(ray)

            rayAngle += FOV / num_rays


    def renderAll(self, screen):
        for ray in self.rays:
            ray.render(screen)

