import pygame
import classes.tile as tile
from classes.ghost import *
from settings import *

class Pacman(pygame.sprite.Sprite):
    def __init__(self, x, y, img, case_size):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.topleft = (case_size * x, case_size * y)
        self.x = x
        self.y = y
        self.case_size = case_size
        self.last_dir = None  # Nouvelle variable

    # Déplacement aléatoire
    # Python
    def move(self, maze, Wall):
        new_x, new_y = self.x, self.y
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            new_x -= 1
        elif keys[pygame.K_RIGHT]:
            new_x += 1
        elif keys[pygame.K_UP]:
            new_y -= 1
        elif keys[pygame.K_DOWN]:
            new_y += 1

        # Vérifie que la case n'est pas un mur
        if not isinstance(maze[new_y][new_x], Wall):
            self.x, self.y = new_x, new_y

        # Effet portail
        if isinstance(maze[self.y][self.x], tile.Portal):
            # Cherche l'autre portail
            portals = [(y, x) for y, line in enumerate(maze) for x, case in enumerate(line) if
                       isinstance(case, tile.Portal)]
            for py, px in portals:
                if (py, px) != (self.y, self.x):
                    self.x, self.y = px, py
                    break

        # Vérifie si Pacman mange un pellet
        if isinstance(maze[self.y][self.x], tile.Pellet):
            maze[self.y][self.x] = tile.Empty()

        return self.x, self.y

    def draw(self, screen, case_size):
        screen.blit(self.image, (case_size * self.x, case_size * self.y))