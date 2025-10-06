from classes.pacman import *
from classes.tile import *
from classes.ghost import *
import settings

class Start():
    def __init__(self, ghost1, ghost2, ghost3, ghost4, pacman):
        self.ghosts = [ghost1, ghost2, ghost3, ghost4]
        self.pacman = pacman

    def start_game(self, maze, count, start_ticks):
        self.ghosts[0].reset(ghostBlue_start_x, ghostBlue_start_y, IMG_GHOSTBLUE_SMALL)
        self.ghosts[1].reset(ghostRed_start_x, ghostRed_start_y, IMG_GHOSTRED_SMALL)
        self.ghosts[2].reset(ghostPink_start_x, ghostPink_start_y, IMG_GHOSTPINK_SMALL)
        self.ghosts[3].reset(ghostOrange_start_x, ghostOrange_start_y, IMG_GHOSTORANGE_SMALL)
        self.pacman.reset(pacman_x, pacman_y, IMG_PACMAN_SMALL)

        for i, line in enumerate(maze):
            for j, case in enumerate(line):
                if isinstance(case, tile.EatenPellet):
                    maze[i][j] = tile.Pellet()
                elif isinstance(case, tile.PowerPellet):
                    case.color = settings.PELLET_COLOR

        count = 0
        start_ticks = pygame.time.get_ticks()
        return count, start_ticks