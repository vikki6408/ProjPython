class Sprite:

    color =

    def draw(self, x, y):
        pygame.draw.rect(settings.SCREEN, settings.PURPLE,
                         (x * settings.CASE_SIZE, y * settings.CASE_SIZE, settings.CASE_SIZE, settings.CASE_SIZE))