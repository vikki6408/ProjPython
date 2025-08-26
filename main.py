import pygame, settings, classes, assets

from classes.mazeClass import initMaze

# pygame setup
pygame.init()

pygame.display.set_caption("Pac-Man")

running = True

# Labyrinthe (1 = mur, 0 = chemin, 2 = porte des fantômes)


# Boucle principale
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    maze = []

    with open("./assets/maze.txt", "r", encoding="utf-8") as f:
        for line in f:
            maze_line = []
            for char in line:
                if char == "0":
                   maze_line.append(Empty())

    initMaze(maze)

pygame.quit()