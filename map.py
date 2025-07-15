import pygame
from settings import *

class Map:
    def __init__(self):
        self.grid = [
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,1,0,0,0,0,0,0,0,0,1,1,0,1],
            [1,0,1,0,0,0,1,0,0,0,0,0,1,0,1],
            [1,0,1,1,1,1,1,0,0,0,0,0,1,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,1,1,1,0,0,0,0,0,0,1,1,1,0,1],
            [1,0,0,0,0,0,0,0,1,0,0,0,0,0,1],
            [1,0,0,0,0,1,1,0,1,0,0,0,0,0,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        ]
    
    def render(self, screen):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                # find pixel coordinates

                tile_x = j * tilesize
                tile_y = i * tilesize

                if self.grid[i][j] == 0:
                    pygame.draw.rect(screen, (255, 255, 255), (tile_x, tile_y, tilesize - 1, tilesize - 1))
                elif self.grid[0][0] == 0:
                    pygame.draw.rect(screen, (400, 400, 400), (tile_x, tile_y, tilesize - 1, tilesize - 1))

    def hasWall(self, x, y):
        return self.grid[int(y // tilesize)][int(x // tilesize)]