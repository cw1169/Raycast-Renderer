import pygame
from settings import *
from map import Map
from player import Player
from raycaster import Raycaster

pygame.init()

screen3D = pygame.display.set_mode((window_width, window_height))

map = Map()
player = Player(map)
raycaster = Raycaster(player, map)

delta_time = 0.1 #allows for frame independant motion
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False

    # fixes framerates about 60 fps
    delta_time = clock.tick(60) / 1000
    delta_time = max(0.001, min(0.1, delta_time))

    screen3D.fill((0, 0, 0))

    player.update()
    raycaster.update()

    raycaster.castAllRays()
    raycaster.renderAll(screen3D)

    pygame.display.update()

pygame.quit() 