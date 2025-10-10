import classes.tile as tile
from settings import *

class Pacman(pygame.sprite.Sprite):
    def __init__(self, x, y, img, case_size):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.topleft = (case_size * x, case_size * y)
        self.x = x
        self.y = y
        self.case_size = case_size
        self.last_dir = None  # Nouvelle variable
        self.lifes = 1
        self.power_mode = False
        self.power_mode_timer = 0
        self.score = 0

    # Déplacement aléatoire
    # Python
    def move(self, maze):
        new_x, new_y = self.x, self.y
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            new_x -= 1
            self.image = IMG_PACMAN_LEFT_SMALL
        elif keys[pygame.K_RIGHT]:
            new_x += 1
            self.image = IMG_PACMAN_RIGHT_SMALL
        elif keys[pygame.K_UP]:
            new_y -= 1
            self.image = IMG_PACMAN_UP_SMALL
        elif keys[pygame.K_DOWN]:
            new_y += 1
            self.image = IMG_PACMAN_DOWN_SMALL

        # Vérifie que la case n'est pas un mur
        if not isinstance(maze[new_y][new_x], tile.Wall):
            self.x, self.y = new_x, new_y

        # Effet portail
        if isinstance(maze[self.y][self.x], tile.Portal):
            # Cherche l'autre portail
            portals = [(y, x) for y, line in enumerate(maze) for x, case in enumerate(line) if
                       isinstance(case, tile.Portal)]
            for py, px in portals:
                if (py, px) != (self.y, self.x):
                    self.x, self.y = px, py
                    break

        # Vérifie si Pacman mange un pellet
        if isinstance(maze[self.y][self.x], tile.Pellet):
            maze[self.y][self.x] = tile.EatenPellet()
            self.score += 10

        # Vérifie si Pacman mange un power pellet
        elif isinstance(maze[self.y][self.x], tile.PowerPellet):
            maze[self.y][self.x] = tile.Empty()
            self.power_mode = True
            self.power_mode_timer = pygame.time.get_ticks()
            self.score += 50

        # Désactive le mode power après 8 secondes
        if self.power_mode and pygame.time.get_ticks() - self.power_mode_timer > 5000:
            self.power_mode = False

        return self.x, self.y

    def draw(self):
        SCREEN.blit(self.image, (CASE_SIZE * self.x, CASE_SIZE * self.y))

    def game_over(self):

        print("Game Over")
        self.x = pacman_x
        self.y = pacman_y

        my_font = pygame.font.SysFont('Comic Sans MS', 50, bold=True)
        text_surface = my_font.render('GAME OVER', True, (255, 0, 0))  # rouge
        text_rect = text_surface.get_rect(center=(SCREEN.get_width() // 2, SCREEN.get_height() // 2))
        SCREEN.blit(text_surface, text_rect)
        pygame.display.update()
        pygame.time.delay(2000)

    def reset(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.lifes = 2
        self.power_mode = False
        self.score = 0
        self.last_dir = None

    def reset_position(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.power_mode = False

    def draw_score(self):
        my_font = pygame.font.SysFont('Comic Sans MS', 24, bold=True)
        text_surface = my_font.render(f'Score : {self.score}', True, (255, 255, 255))
        SCREEN.blit(text_surface, (5, 10))  # Position en haut à gauche

    def draw_lifes(self):
        img = IMG_PACMAN_RIGHT_SMALL
        for i in range(self.lifes, 5 + self.lifes * 25, 25):
            SCREEN.blit(img, (i + 1, 45))

    # Vérifie la victoire
    def check_win(self, maze):
        for line in maze:
            for case in line:
                if isinstance(case, tile.Pellet) or isinstance(case, tile.PowerPellet):
                    return
        my_font = pygame.font.SysFont('Comic Sans MS', 50, bold=True)
        text_surface = my_font.render('VICTORY', True, (0, 255, 0))
        text_rect = text_surface.get_rect(center=(SCREEN.get_width() // 2, SCREEN.get_height() // 2))
        SCREEN.blit(text_surface, text_rect)
        pygame.display.update()
        pygame.time.delay(2000)
        return True

