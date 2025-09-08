import pygame
from settings import *
from classes.tile import *

#from classes.mazeClass import initMaze

# pygame setup
pygame.init()

pygame.display.set_caption("Pac-Man")

IMAGE_SMALL = pygame.transform.scale(IMG, (CASE_SIZE, CASE_SIZE))

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
        elif event.type == pygame.KEYDOWN:
            new_x, new_y = pacman_x, pacman_y
            if event.key == pygame.K_LEFT:
                new_x -= 1
            elif event.key == pygame.K_RIGHT:
                new_x += 1
            elif event.key == pygame.K_UP:
                new_y -= 1
            elif event.key == pygame.K_DOWN:
                new_y += 1
            # Vérifie que la case n'est pas un mur
            if not isinstance(maze[new_y][new_x], Wall):
                pacman_x, pacman_y = new_x, new_y

    SCREEN.fill(BACKGROUND_COLOR)
    for y, line in enumerate(maze):
        for x, case in enumerate(line):
            case.draw(x, y)
    SCREEN.blit(IMAGE_SMALL, (CASE_SIZE * pacman_x, CASE_SIZE * pacman_y))
    pygame.display.flip()

pygame.quit()