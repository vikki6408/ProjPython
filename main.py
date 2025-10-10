from classes.restart import *
from classes.ghost import *
from classes.pacman import *
from classes.tile import *
from settings import *

# pygame setup
pygame.init()
pygame.display.set_caption("Pac-Man")

# Pygame clock
clock = pygame.time.Clock()
start_ticks=pygame.time.get_ticks()
previous_time = pygame.time.get_ticks()

# Initialisation of sprites
ghost1 = Ghost(ghostBlue_start_x, ghostBlue_start_y, IMG_GHOSTBLUE_SMALL, CASE_SIZE)
ghost2 = Ghost(ghostRed_start_x, ghostRed_start_y, IMG_GHOSTRED_SMALL, CASE_SIZE)
ghost3 = Ghost(ghostPink_start_x, ghostPink_start_y, IMG_GHOSTPINK_SMALL, CASE_SIZE)
ghost4 = Ghost(ghostOrange_start_x, ghostOrange_start_y, IMG_GHOSTORANGE_SMALL, CASE_SIZE)
pacman = Pacman(pacman_x, pacman_y, IMG_PACMAN_RIGHT_SMALL, CASE_SIZE)
restart = Restart(ghost1, ghost2, ghost3, ghost4, pacman)

# variable
ghosts = [
    ghost1,
    ghost2,
    ghost3,
    ghost4
]

count = 1
running = True

# Maze
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

# Main loop
while running:
    # Event management
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    seconds = (pygame.time.get_ticks() - start_ticks) / 1000
    SCREEN.fill(BACKGROUND_COLOR)

    # Ghost outing
    if count == 1:
        if seconds > 5:
            ghost1.x = 23
            ghost1.y = 12
            count += 1
    if count == 2:
        if seconds > 11:
            ghost3.x = 23
            ghost3.y = 12
            count += 1
    if count == 3:
        if seconds > 17:
            ghost4.x = 23
            ghost4.y = 12
            count += 1


    for y, line in enumerate(maze):
        for x, case in enumerate(line):
            case.draw(x, y)

    # Ghost scared, pacman mode power
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

    # Moving sprites
    pacman.move(maze)
    for ghost in ghosts:
        ghost.move(maze)
        ghost.update_waiting()
        if pacman.x == ghost.x and pacman.y == ghost.y:
            if ghost.scared and pacman.power_mode:
                pacman.score += 200
                ghost.start_waiting()
                ghost.scared = False
                ghost.image = ghost.original_image
            else:
                if pacman.lifes < 0:
                    pacman.game_over()
                    restart.restart_game(maze)
                else:
                    pacman.lifes -= 1
                    pacman.draw_lifes()
                    restart.reset_sprites_positions()
                    count = 1
                    start_ticks = pygame.time.get_ticks()

    # Displaying sprites
    pacman.draw()
    for ghost in ghosts:
        ghost.draw()

    # Check win
    if pacman.check_win(maze):
        restart.reset_sprites_positions()
        count = 1
        start_ticks = pygame.time.get_ticks()
        # Put the pellets back in the maze
        for i, line in enumerate(maze):
            for j, case in enumerate(line):
                if isinstance(case, tile.EatenPellet):
                    maze[i][j] = tile.Pellet()
                elif isinstance(case, tile.PowerPellet):
                    case.color = settings.PELLET_COLOR

    # Draw score and lifes
    pacman.draw_score()
    pacman.draw_lifes()

    # Refresh the display
    pygame.display.flip()

    # Loop speed
    clock.tick(6)

pygame.quit()