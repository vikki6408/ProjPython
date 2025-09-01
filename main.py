import pygame
from settings import *
from classes.tile import *

#from classes.mazeClass import initMaze

# pygame setup
pygame.init()

pygame.display.set_caption("Pac-Man")

img = pygame.image.load('assets/images/pacman.png')
IMAGE_SMALL = pygame.transform.scale(img, (CASE_SIZE, CASE_SIZE))

running = True

# Labyrinthe (1 = mur, 0 = chemin, 2 = porte des fantômes)
maze = []
with open("assets/maze.txt", "r", encoding="utf-8") as f:
    for line in f:
        maze_line = []
        for char in line:
            if char == " ":
                maze_line.append(Empty())
            elif char == "|":
                maze_line.append(Wall())
            elif char == "*":
                maze_line.append(Pellet())
        maze.append(maze_line)

# Boucle principale
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    print("Drawing maze")
    SCREEN.fill(BACKGROUND_COLOR)
    for y, line in enumerate(maze):
        for x, case in enumerate(line):
            print(f"drawing {x} {y} {case}")
            case.draw(x, y)
            SCREEN.blit(IMAGE_SMALL, (CASE_SIZE * 13, CASE_SIZE * 23))
    pygame.display.flip()

pygame.quit()