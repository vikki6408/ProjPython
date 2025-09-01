import pygame

TITLE = 'Pac-Man'
CASE_SIZE = 18
WIDTH, HEIGHT = 28, 32

SCREEN = pygame.display.set_mode((WIDTH * CASE_SIZE, HEIGHT * CASE_SIZE))

# Couleurs
BACKGROUND_COLOR = (1, 28, 40)
WALL_COLOR =   (61, 88, 242)
PELLET_COLOR = (242, 203, 5)  #235, 245, 0    #F2CB05

RED = (255, 0, 0)
LIGHT_BLUE = (4, 178, 249)