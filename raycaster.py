import math, pygame
from settings import *
from ray import Ray

class Raycaster:
    def __init__(self, player, map):
        self.rays = []
        self.player = player
        self.map = map
        self.type = 'line'
    
    def castAllRays(self):
        self.rays = []
        rayAngle = (self.player.rotation_angle - FOV / 2)
        for i in range(num_rays):
            ray = Ray(rayAngle, self.player, self.map)
            ray.cast()
            self.rays.append(ray)

            rayAngle += FOV / num_rays

    
    def update(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LSHIFT] and self.type == 'line':
            self.type = 'trace'
        elif keys_pressed[pygame.K_LSHIFT] and self.type == 'trace':
            self.type = 'line'


    def renderAll(self, screen):
        for ray in self.rays:
            ray.render(screen, self.type)


