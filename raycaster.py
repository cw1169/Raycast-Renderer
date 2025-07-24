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
        i = 1
        for ray in self.rays:
            # Render 3d walls
            # (Projected Wall Height / distance to projection plain) = (wall height / distance to wall)
            line_height = (wall_height / ray.distance) * 415
            draw_begin = (window_height / 2) - (line_height / 2)
            draw_end = line_height
            pygame.draw.rect(screen, (255, 255, 255), (i*res, draw_begin, res, draw_end))
            i += 1


            # Calls function to render 2D Rays
            # ray.render(screen, self.type)