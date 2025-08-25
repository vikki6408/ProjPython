import pygame

# pygame setup
pygame.init()
TAILLE_CASE = 30
LARGEUR, HAUTEUR = 30, 20
SCREEN = pygame.display.set_mode((LARGEUR * TAILLE_CASE, HAUTEUR * TAILLE_CASE))
pygame.display.set_caption("Labyrinthe Pac-Man")
clock = pygame.time.Clock()
running = True


# Couleurs
NOIR = (0, 0, 0)
BLEU = (0, 0, 255)

# Labyrinthe (1 = mur, 0 = chemin)
labyrinthe = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

# Boucle principale

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    SCREEN.fill(NOIR)

    # Dessiner le labyrinthe
    for y, ligne in enumerate(labyrinthe):
        for x, case in enumerate(ligne):
            if case == 1:
                pygame.draw.rect(SCREEN, BLEU, (x*TAILLE_CASE, y*TAILLE_CASE, TAILLE_CASE, TAILLE_CASE))

    pygame.display.flip()


pygame.quit()