import pygame
import random
import classes.tile as tile
from settings import CASE_SIZE, SCREEN


class Ghost(pygame.sprite.Sprite):
    def __init__(self, x, y, img, case_size):
        super().__init__()
        self.image = img
        self.original_image = img
        self.rect = self.image.get_rect()
        self.rect.topleft = (case_size * x, case_size * y)
        self.x = x
        self.y = y
        self.start_x = x
        self.start_y = y
        self.case_size = case_size
        self.last_dir = None
        self.scared = False
        self.waiting = False
        self.wait_start_time = 0
        self.move_delay = 180
        self.last_move_time = pygame.time.get_ticks()

    def move(self, maze):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_move_time < self.move_delay:
            return
        self.last_move_time = current_time

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        if self.last_dir:
            directions.remove((-self.last_dir[0], -self.last_dir[1]))
            random.shuffle(directions)

        for dx, dy in directions:
            new_x = self.x + dx
            new_y = self.y + dy
            if not isinstance(maze[new_y][new_x], tile.Wall):
                self.x, self.y = new_x, new_y
                self.rect.topleft = (self.case_size * self.x, self.case_size * self.y)
                self.last_dir = (dx, dy)
                break

        # Effet portail
        if isinstance(maze[self.y][self.x], tile.Portal):
            portals = [(y, x) for y, line in enumerate(maze) for x, case in enumerate(line) if
                       isinstance(case, tile.Portal)]
            for py, px in portals:
                if (py, px) != (self.y, self.x):
                    self.x, self.y = px, py
                    self.rect.topleft = (self.case_size * self.x, self.case_size * self.y)
                    break

    def draw(self):
        SCREEN.blit(self.image, (CASE_SIZE * self.x, CASE_SIZE * self.y))


    def reset(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.scared = False

    def start_waiting(self):
        self.x = 23
        self.y = 12
        self.waiting = True
        self.wait_start_time = pygame.time.get_ticks()

    def update_waiting(self):
        if self.waiting and pygame.time.get_ticks() - self.wait_start_time > 2000:
            self.x = 23
            self.y = 12
            self.waiting = False