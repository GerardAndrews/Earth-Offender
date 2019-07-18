import pygame

WHITE = (255, 255, 255)


class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # STARS
        self.image = pygame.Surface([2, 2])
        self.image.fill(WHITE)

        self.rect = self.image.get_rect()