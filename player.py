import pygame
import math
from settings import *
from enum import Enum


class Player:
    def __init__(self):
        self.x = window_width / 2
        self.y = window_height / 2
        self.player_radius = 5
        self.rotation_angle = 45 * (math.pi / 180)
        self.rotation_speed = 5 * (math.pi / 180)
        self.turn_direction = 0
        self.walk_direction = 0
        self.move_speed = 2.5

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
        self.rotation_angle +=  self.turn_direction * self.rotation_speed

        self.x += math.cos(self.rotation_angle) * movestep
        self.y += math.sin(self.rotation_angle) * movestep


    def render(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), self.player_radius)
        pygame.draw.line(screen, (255, 0, 255), (self.x, self.y), (self.x + math.cos(self.rotation_angle) * 50, self.y + math.sin(self.rotation_angle) * 50))