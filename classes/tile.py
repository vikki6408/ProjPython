import settings
import pygame

class Tile:
    def draw(self, x, y):
        pygame.draw.rect(settings.SCREEN, self.color,
                         (x * settings.CASE_SIZE, y * settings.CASE_SIZE, settings.CASE_SIZE, settings.CASE_SIZE))

class Empty(Tile):
    def __init__(self):
        self.color = settings.BACKGROUND_COLOR

class Wall(Tile):
    def __init__(self):
        self.color = settings.WALL_COLOR

class Pellet(Tile):
    def __init__(self):
        self.color = settings.PELLET_COLOR

    def draw(self, x, y):
        pygame.draw.circle(settings.SCREEN, self.color, (x * settings.CASE_SIZE + 9, y * settings.CASE_SIZE + 9), 3)

class PowerPellet(Tile):
    def __init__(self):
        self.color = settings.PELLET_COLOR

    def draw(self, x, y):
        pygame.draw.circle(settings.SCREEN, self.color, (x * settings.CASE_SIZE + 9, y * settings.CASE_SIZE + 9), 6)

class Portal(Tile):
    def __init__(self):
        self.color = settings.BACKGROUND_COLOR
