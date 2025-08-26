import pygame
import settings



# Dessiner le labyrinthe

def initMaze(maze) :
    settings.SCREEN.fill(settings.BLACK)
    for y, line in enumerate(maze):
        for x, case in enumerate(maze):
            case.draw(x, y);
            if case == 1:
                pygame.draw.rect(settings.SCREEN, settings.PURPLE, (x * settings.CASE_SIZE, y * settings.CASE_SIZE, settings.CASE_SIZE, settings.CASE_SIZE))
            if case == 3:
                pygame.draw.circle(settings.SCREEN, settings.YELLOW, (x * settings.CASE_SIZE + 8, y * settings.CASE_SIZE + 8), 4)
    pygame.display.flip()