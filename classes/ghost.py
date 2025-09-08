import pygame
import random
class Ghost(pygame.sprite.Sprite):
    def __init__(self, x, y, img, case_size):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.topleft = (case_size * x, case_size * y)
        self.x = x
        self.y = y
        self.case_size = case_size
        self.last_dir = None  # Nouvelle variable

    def move(self, maze, Wall):
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        if self.last_dir:
            # On évite le mouvement inverse
            directions.remove((-self.last_dir[0], -self.last_dir[1]))
        random.shuffle(directions)
        for dx, dy in directions:
            new_x = self.x + dx
            new_y = self.y + dy
            if not isinstance(maze[new_y][new_x], Wall):
                self.x, self.y = new_x, new_y
                self.rect.topleft = (self.case_size * self.x, self.case_size * self.y)
                self.last_dir = (dx, dy)
                break

    def draw(self, screen, case_size):
        screen.blit(self.image, (case_size * self.x, case_size * self.y))
