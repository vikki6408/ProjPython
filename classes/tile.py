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
        center = settings.CASE_SIZE // 2
        pygame.draw.circle(
            settings.SCREEN,
            self.color,
            (x * settings.CASE_SIZE + center, y * settings.CASE_SIZE + center),
            4
        )
class PowerPellet(Tile):
    def __init__(self):
        self.color = settings.PELLET_COLOR

    def draw(self, x, y):
        center = settings.CASE_SIZE // 2
        pygame.draw.circle(
            settings.SCREEN,
            self.color,
            (x * settings.CASE_SIZE + center, y * settings.CASE_SIZE + center),
            9
        )
class Portal(Tile):
    def __init__(self):
        self.color = settings.BACKGROUND_COLOR

class EatenPellet(Tile):
    def __init__(self):
        self.color = settings.BACKGROUND_COLOR