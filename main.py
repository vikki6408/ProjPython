from classes.restart import *
# pygame setup

pygame.init()
pygame.display.set_caption("Pac-Man")
clock = pygame.time.Clock()
count = 1
start_ticks=pygame.time.get_ticks()

# Vitesse de déplacement (en pixels par seconde)
PACMAN_SPEED = 100  # Ajustez cette valeur pour Pac-Man
GHOST_SPEED = 80    # Ajustez cette valeur pour les fantômes

# Temps précédent pour calculer delta_time
previous_time = pygame.time.get_ticks()

running = True

ghost1 = Ghost(ghostBlue_start_x, ghostBlue_start_y, IMG_GHOSTBLUE_SMALL, CASE_SIZE)
ghost2 = Ghost(ghostRed_start_x, ghostRed_start_y, IMG_GHOSTRED_SMALL, CASE_SIZE)
ghost3 = Ghost(ghostPink_start_x, ghostPink_start_y, IMG_GHOSTPINK_SMALL, CASE_SIZE)
ghost4 = Ghost(ghostOrange_start_x, ghostOrange_start_y, IMG_GHOSTORANGE_SMALL, CASE_SIZE)

pacman = Pacman(pacman_x, pacman_y, IMG_PACMAN_RIGHT_SMALL, CASE_SIZE)

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
        if seconds > 8:
            ghost1.x = 23
            ghost1.y = 12
            count += 1
    if count == 2:
        if seconds > 17:
            ghost3.x = 23
            ghost3.y = 12
            count += 1
    if count == 3:
        if seconds > 27:
            ghost4.x = 23
            ghost4.y = 12
            count += 1

    SCREEN.fill(BACKGROUND_COLOR)
    for y, line in enumerate(maze):
        for x, case in enumerate(line):
            case.draw(x, y)

    # Met les fantômes en mode effrayé si Pacman est en mode power ou les réinitialise si plus
    if pacman.power_mode:
        for ghost in ghosts:
            ghost.scared = True
            ghost.image = IMG_GHOSTSCARED
    else:
        for i, ghost in enumerate(ghosts):
            if i == 0:
                ghost.image = IMG_GHOSTBLUE_SMALL
            elif i == 1:
                ghost.image = IMG_GHOSTRED_SMALL
            elif i == 2:
                ghost.image = IMG_GHOSTPINK_SMALL
            elif i == 3:
                ghost.image = IMG_GHOSTORANGE_SMALL
            ghost.scared = False

    # Affichage des sprites
    pacman.move(maze, tile.Wall)
    pacman.draw(SCREEN, CASE_SIZE)
    for ghost in ghosts:
        ghost.draw(SCREEN, CASE_SIZE)
        ghost.move(maze, tile.Wall)
        ghost.update_waiting() # Met à jour l'état d'attente du fantôme
        if pacman.x == ghost.x and pacman.y == ghost.y:
            if ghost.scared and pacman.power_mode:
                # Pacman mange le fantôme, le renvoie à sa position de départ
                pacman.score += 200
                ghost.start_waiting()
                ghost.scared = False
                ghost.image = ghost.original_image
            else:
                if pacman.lifes < 0:
                    pacman.game_over(SCREEN)
                    restart.restart_game(maze)
                else:
                    pacman.draw_lifes(SCREEN)
                    pacman.lifes -= 1
                    restart.reset_sprites_positions()
                    count = 1
                    start_ticks = pygame.time.get_ticks()

    # Vérifie si Pacman a gagné
    if pacman.check_win(maze):
        restart.restart_game(maze)

    # Affiche le score
    pacman.draw_score(SCREEN)
    pacman.draw_lifes(SCREEN)

    # Actualise l'affichage
    pygame.display.flip()
    print(count)
    print(seconds)

    # Vitesse de la boucle
    clock.tick(6)
pygame.quit()