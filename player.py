import pygame
import math
from settings import *

class Player:
    def __init__(self, map):
        self.x = window_width / 2
        self.y = window_height / 2
        self.player_radius = 5
        self.rotation_angle = 45 * (math.pi / 180)
        self.rotation_speed = 5 * (math.pi / 180)
        self.turn_direction = 0
        self.walk_direction = 0
        self.move_speed = 2.5
        self.map = map

    def update(self):
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_RIGHT]:
            self.turn_direction = 1
        elif keys_pressed[pygame.K_LEFT]:
            self.turn_direction = -1
        else:
            self.turn_direction = 0
        
        if keys_pressed[pygame.K_UP]:
            self.walk_direction = 1
        elif keys_pressed[pygame.K_DOWN]:
            self.walk_direction = -1
        else:
            self.walk_direction = 0

        movestep = self.move_speed * self.walk_direction
        next_x = self.x + math.cos(self.rotation_angle) * movestep
        next_y = self.y + math.sin(self.rotation_angle) * movestep

        grid_x = int(next_x / tilesize)
        grid_y = int(next_y / tilesize)

        if 0 <= grid_x < cols and 0 <= grid_y < rows:
            if self.map.grid[grid_y][grid_x] == 0:
                self.x = next_x
                self.y = next_y
        else:
            pass

        self.rotation_angle += self.turn_direction * self.rotation_speed

        self.x += math.cos(self.rotation_angle) * movestep
        self.y += math.sin(self.rotation_angle) * movestep


    def render(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), self.player_radius)
        pygame.draw.line(screen, (255, 0, 255), (self.x, self.y), (self.x + math.cos(self.rotation_angle) * 50, self.y + math.sin(self.rotation_angle) * 50))