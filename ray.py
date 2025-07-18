import pygame, math

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
        ray_coords = [self.player.x, self.player.y]
        while self.map.hasWall(ray_coords[0], ray_coords[1]) == False:
            ray_coords[0] += 1
            ray_coords[1] += 1
            self.distance += 1


    def render(self, screen):
        # Temporary 
        pygame.draw.line(screen, (255, 0, 0), (self.player.x, self.player.y), (self.player.x + math.cos(self.rayAngle) * self.distance, self.player.y + math.sin(self.rayAngle) * self.distance))