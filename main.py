from settings import *
from classes.tile import *

# pygame setup
pygame.init()

pygame.display.set_caption("Pac-Man")

# Redimension de pacman
IMG_PACMAN_SMALL = pygame.transform.scale(IMG_PACMAN, (CASE_SIZE, CASE_SIZE))
# Redimension des fantômes
IMG_GHOSTBLUE_SMALL = pygame.transform.scale(IMG_GHOSTBLUE, (CASE_SIZE, CASE_SIZE))
IMG_GHOSTRED_SMALL = pygame.transform.scale(IMG_GHOSTRED, (CASE_SIZE, CASE_SIZE))
IMG_GHOSTPINK_SMALL = pygame.transform.scale(IMG_GHOSTPINK, (CASE_SIZE, CASE_SIZE))
IMG_GHOSTORANGE_SMALL = pygame.transform.scale(IMG_GHOSTORANGE, (CASE_SIZE, CASE_SIZE))

clock = pygame.time.Clock()
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

    new_x, new_y = pacman_x, pacman_y
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
        pacman_x, pacman_y = new_x, new_y

    SCREEN.fill(BACKGROUND_COLOR)
    for y, line in enumerate(maze):
        for x, case in enumerate(line):
            case.draw(x, y)
    # Affichage des sprites
    SCREEN.blit(IMG_PACMAN_SMALL, (CASE_SIZE * pacman_x, CASE_SIZE * pacman_y))
    SCREEN.blit(IMG_GHOSTBLUE_SMALL, (CASE_SIZE * ghostBlue_start_x, CASE_SIZE * ghostBlue_start_y))
    SCREEN.blit(IMG_GHOSTRED_SMALL, (CASE_SIZE * ghostRed_start_x, CASE_SIZE * ghostRed_start_y))
    SCREEN.blit(IMG_GHOSTPINK_SMALL, (CASE_SIZE * ghostPink_start_x, CASE_SIZE * ghostPink_start_y))
    SCREEN.blit(IMG_GHOSTORANGE_SMALL, (CASE_SIZE * ghostOrange_start_x, CASE_SIZE * ghostOrange_start_y))

    pygame.display.flip()
    clock.tick(6)
pygame.quit()