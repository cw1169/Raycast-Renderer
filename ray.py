import pygame, math
from settings import *

def normalizeAngle(angle):
    angle = angle % (2 * math.pi)
    if angle < 0:
        angle = (2 * math.pi) + angle
    return angle

class Ray:
    def __init__(self, angle, player, map):
        self.rayAngle = normalizeAngle(angle)
        self.player = player
        self.map = map
        self.distance = 0

    def cast(self):
        # Setup
        ray_x = self.player.x
        ray_y = self.player.y

        ray_angle = normalizeAngle(self.rayAngle)

        sin_a = math.sin(ray_angle)
        cos_a = math.cos(ray_angle)

        # Step size
        step_size = 1
        distance = 0

        while True:
            ray_x += cos_a * step_size
            ray_y += sin_a * step_size
            distance += step_size

            map_x = int(ray_x / tilesize)
            map_y = int(ray_y / tilesize)

            # Stop if out of bounds
            if map_x < 0 or map_x >= cols or map_y < 0 or map_y >= rows:
                break

            # Stop if hit a wall
            if self.map.grid[map_y][map_x] == 1:
                break

        # Store ray hit location
        self.hit_x = ray_x
        self.hit_y = ray_y



    def render(self, screen):
        pygame.draw.line(screen, (255, 0, 0), (self.player.x, self.player.y), (self.hit_x, self.hit_y))
