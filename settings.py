import pygame

TITLE = 'Pac-Man'
CASE_SIZE = 18
WIDTH, HEIGHT = 28, 32

# Position initiale de Pac-Man
pacman_x, pacman_y = 13, 23
# Position initiale des fantômes
ghostBlue_start_x, ghostBlue_start_y = 11, 14
ghostRed_start_x, ghostRed_start_y = 13, 11
ghostPink_start_x, ghostPink_start_y = 13, 14
ghostOrange_start_x, ghostOrange_start_y = 15, 14

#pacman image
IMG_PACMAN = pygame.image.load('assets/images/pacman.png')

#ghosts image
IMG_GHOSTBLUE = pygame.image.load('assets/images/ghostBlue.png')
IMG_GHOSTRED = pygame.image.load('assets/images/ghostRed.png')
IMG_GHOSTPINK = pygame.image.load('assets/images/ghostPink.png')
IMG_GHOSTORANGE = pygame.image.load('assets/images/ghostOrange.png')

SCREEN = pygame.display.set_mode((WIDTH * CASE_SIZE, HEIGHT * CASE_SIZE))

# Couleurs
BACKGROUND_COLOR = (1, 28, 40)
WALL_COLOR =   (61, 88, 242)
PELLET_COLOR = (242, 203, 5)  #235, 245, 0    #F2CB05

RED = (255, 0, 0)
LIGHT_BLUE = (4, 178, 249)