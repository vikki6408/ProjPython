from settings import *
from classes.tile import *
from classes.ghost import *

# pygame setup
pygame.init()
pygame.display.set_caption("Pac-Man")
clock = pygame.time.Clock()
count = 1
start_ticks=pygame.time.get_ticks()

running = True

# Redimension de pacman
IMG_PACMAN_SMALL = pygame.transform.scale(IMG_PACMAN, (CASE_SIZE, CASE_SIZE))

# Redimension des fantômes
IMG_GHOSTBLUE_SMALL = pygame.transform.scale(IMG_GHOSTBLUE, (CASE_SIZE, CASE_SIZE))
IMG_GHOSTRED_SMALL = pygame.transform.scale(IMG_GHOSTRED, (CASE_SIZE, CASE_SIZE))
IMG_GHOSTPINK_SMALL = pygame.transform.scale(IMG_GHOSTPINK, (CASE_SIZE, CASE_SIZE))
IMG_GHOSTORANGE_SMALL = pygame.transform.scale(IMG_GHOSTORANGE, (CASE_SIZE, CASE_SIZE))


ghost1 = Ghost(ghostBlue_start_x, ghostBlue_start_y, IMG_GHOSTBLUE_SMALL, CASE_SIZE)
ghost2 =  Ghost(ghostRed_start_x, ghostRed_start_y, IMG_GHOSTRED_SMALL, CASE_SIZE)
ghost3 = Ghost(ghostPink_start_x, ghostPink_start_y, IMG_GHOSTPINK_SMALL, CASE_SIZE)
ghost4 = Ghost(ghostOrange_start_x, ghostOrange_start_y, IMG_GHOSTORANGE_SMALL, CASE_SIZE)

# Création des fantômes
ghosts = [
    ghost1,
    ghost2,
    ghost3,
    ghost4
]



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

    seconds = (pygame.time.get_ticks() - start_ticks) / 1000
    print(seconds)

    if count == 1:
        if seconds > 8:  # if more than 10 seconds close the game
            ghost1.x = 13
            ghost1.y = 11
            count += 1
    if count == 2:
        if seconds > 17:
            ghost3.x = 13
            ghost3.y = 11
            count += 1
    if count == 3:
        if seconds > 27:
            ghost4.x = 13
            ghost4.y = 11
            count += 1
    # Gestion des déplacements de Pacman
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

    # Vérifie si Pacman mange un pellet
    if isinstance(maze[pacman_y][pacman_x], Pellet):
        maze[pacman_y][pacman_x] = Empty()
        # score += 1  # (optionnel, si tu as une variable score)

    # Vérifie que la case n'est pas un mur
    if not isinstance(maze[new_y][new_x], Wall):
        pacman_x, pacman_y = new_x, new_y

    SCREEN.fill(BACKGROUND_COLOR)
    for y, line in enumerate(maze):
        for x, case in enumerate(line):
            case.draw(x, y)

    # Affichage des sprites
    SCREEN.blit(IMG_PACMAN_SMALL, (CASE_SIZE * pacman_x, CASE_SIZE * pacman_y))
    for ghost in ghosts:
        ghost.draw(SCREEN, CASE_SIZE)
        ghost.move(maze, Wall) # calculate how many seconds

    # Actualise l'affichage
    pygame.display.flip()

    # Vitesse de la boucle
    clock.tick(6)
pygame.quit()