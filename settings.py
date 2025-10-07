import pygame

TITLE = 'Pac-Man'
CASE_SIZE = 20
WIDTH, HEIGHT = 48, 34

# Position initiale de Pac-Man
pacman_x, pacman_y = 23, 24
# Position initiale des fantômes
ghostBlue_start_x, ghostBlue_start_y = 21, 15
ghostRed_start_x, ghostRed_start_y = 23, 12
ghostPink_start_x, ghostPink_start_y = 23, 15
ghostOrange_start_x, ghostOrange_start_y = 25, 15

#pacman image
IMG_PACMAN_LEFT = pygame.image.load('./assets/images/pacman_left.png')
IMG_PACMAN_RIGHT = pygame.image.load('./assets/images/pacman_right.png')
IMG_PACMAN_DOWN = pygame.image.load('./assets/images/pacman_down.png')
IMG_PACMAN_UP = pygame.image.load('./assets/images/pacman_up.png')


#ghosts image
IMG_GHOSTBLUE = pygame.image.load('assets/images/ghostBlue.png')
IMG_GHOSTRED = pygame.image.load('assets/images/ghostRed.png')
IMG_GHOSTPINK = pygame.image.load('assets/images/ghostPink.png')
IMG_GHOSTORANGE = pygame.image.load('assets/images/ghostOrange.png')
IMG_GHOSTSCARED = pygame.image.load('assets/images/ghostScared.png')

IMG_PACMAN_LEFT_SMALL = pygame.transform.scale(IMG_PACMAN_LEFT, (CASE_SIZE, CASE_SIZE))
IMG_PACMAN_RIGHT_SMALL = pygame.transform.scale(IMG_PACMAN_RIGHT, (CASE_SIZE, CASE_SIZE))
IMG_PACMAN_DOWN_SMALL = pygame.transform.scale(IMG_PACMAN_DOWN, (CASE_SIZE, CASE_SIZE))
IMG_PACMAN_UP_SMALL = pygame.transform.scale(IMG_PACMAN_UP, (CASE_SIZE, CASE_SIZE))

# Redimension des fantômes
IMG_GHOSTBLUE_SMALL = pygame.transform.scale(IMG_GHOSTBLUE, (CASE_SIZE, CASE_SIZE))
IMG_GHOSTRED_SMALL = pygame.transform.scale(IMG_GHOSTRED, (CASE_SIZE, CASE_SIZE))
IMG_GHOSTPINK_SMALL = pygame.transform.scale(IMG_GHOSTPINK, (CASE_SIZE, CASE_SIZE))
IMG_GHOSTORANGE_SMALL = pygame.transform.scale(IMG_GHOSTORANGE, (CASE_SIZE, CASE_SIZE))
IMG_GHOSTSCARED = pygame.transform.scale(IMG_GHOSTSCARED, (CASE_SIZE, CASE_SIZE))

SCREEN = pygame.display.set_mode((WIDTH * CASE_SIZE, HEIGHT * CASE_SIZE))

# Couleurs
BACKGROUND_COLOR = (1, 28, 40)
WALL_COLOR = (61, 88, 242)
PELLET_COLOR = (242, 203, 5)  #235, 245, 0    #F2CB05

RED = (255, 0, 0)
LIGHT_BLUE = (4, 178, 249)