from classes.ghost import *
from settings import *
from classes.restart import *
import classes.pacman as pacman
import classes.tile as tile

# pygame setup
pygame.init()
pygame.display.set_caption("Pac-Man")
clock = pygame.time.Clock()
count = 1
power_mode = False
power_mode_timer = 0
start_ticks=pygame.time.get_ticks()


running = True

# Redimension de pacman

ghost1 = Ghost(ghostBlue_start_x, ghostBlue_start_y, IMG_GHOSTBLUE_SMALL, CASE_SIZE)
ghost2 =  Ghost(ghostRed_start_x, ghostRed_start_y, IMG_GHOSTRED_SMALL, CASE_SIZE)
ghost3 = Ghost(ghostPink_start_x, ghostPink_start_y, IMG_GHOSTPINK_SMALL, CASE_SIZE)
ghost4 = Ghost(ghostOrange_start_x, ghostOrange_start_y, IMG_GHOSTORANGE_SMALL, CASE_SIZE)

pacman = pacman.Pacman(pacman_x, pacman_y, IMG_PACMAN_SMALL, CASE_SIZE)

# Création des fantômes
ghosts = [
    ghost1,
    ghost2,
    ghost3,
    ghost4
]
restart = Restart(ghost1, ghost2, ghost3, ghost4, pacman)

# Labyrinthe (1 = mur, 0 = chemin, 2 = porte des fantômes)
maze = []
with open("assets/maze.txt", "r", encoding="utf-8") as f:
    for line in f:
        maze_line = []
        for char in line:
            if char == " ":
                maze_line.append(tile.Empty())
            elif char == "|":
                maze_line.append(tile.Wall())
            elif char == "*":
                maze_line.append(tile.Pellet())
            elif char == "$":
                maze_line.append(tile.PowerPellet())
            elif char == "¦":
                maze_line.append(tile.Portal())
        maze.append(maze_line)

# Boucle principale
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    seconds = (pygame.time.get_ticks() - start_ticks) / 1000

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

    SCREEN.fill(BACKGROUND_COLOR)
    for y, line in enumerate(maze):
        for x, case in enumerate(line):
            case.draw(x, y)

    pacman.draw(SCREEN, CASE_SIZE)
    pacman.move(maze, tile.Wall)

    # Affichage des sprites
    for ghost in ghosts:
        ghost.draw(SCREEN, CASE_SIZE)
        ghost.move(maze, tile.Wall)
        if pacman.x == ghost.x and pacman.y == ghost.y:
            if ghost.scared:
                # Pacman mange le fantôme, le renvoie à sa position de départ
                ghost.x = ghost.start_x
                ghost.y = ghost.start_y
                ghost.scared = False
                ghost.image = ghost.original_image
            else:
                # Pacman est touché, fin du jeu ou réinitialisation
                pacman.game_over(SCREEN)  # ou réinitialise la position de Pacman
                restart.restart_game()

    # Vérifie si Pacman mange un power pellet
    if isinstance(maze[pacman.y][pacman.x], tile.PowerPellet):
        maze[pacman.y][pacman.x] = tile.Empty()
        power_mode = True
        power_mode_timer = pygame.time.get_ticks()
        for ghost in ghosts:
            ghost.scared = True
            ghost.image = IMG_GHOSTSCARED

    # Désactive le mode effrayé après 8 secondes
    if power_mode and pygame.time.get_ticks() - power_mode_timer > 8000:
        power_mode = False
        for ghost, img in zip(ghosts,
                              [IMG_GHOSTBLUE_SMALL, IMG_GHOSTRED_SMALL, IMG_GHOSTPINK_SMALL, IMG_GHOSTORANGE_SMALL]):
            ghost.scared = False
            ghost.image = img

    # Actualise l'affichage
    pygame.display.flip()

    # Vitesse de la boucle
    clock.tick(6)
pygame.quit()