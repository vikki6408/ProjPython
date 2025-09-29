from settings import *
from classes.ghost import *
from classes.pacman import *

class Restart():
    def __init__(self, ghost1, ghost2, ghost3, ghost4, pacman):
        self.ghosts = [ghost1, ghost2, ghost3, ghost4]
        self.pacman = pacman

    def restart_game(self):
        self.ghosts[0].reset(ghostBlue_start_x, ghostBlue_start_y, IMG_GHOSTBLUE_SMALL)
        self.ghosts[1].reset(ghostRed_start_x, ghostRed_start_y, IMG_GHOSTRED_SMALL)
        self.ghosts[2].reset(ghostPink_start_x, ghostPink_start_y, IMG_GHOSTPINK_SMALL)
        self.ghosts[3].reset(ghostOrange_start_x, ghostOrange_start_y, IMG_GHOSTORANGE_SMALL)
        self.pacman.reset(pacman_x, pacman_y, IMG_PACMAN_SMALL)
