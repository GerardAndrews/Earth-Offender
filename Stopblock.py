import pygame

PINK = (255, 0, 255)


class StopBlock(pygame.sprite.Sprite):
    """ This class represents the block. """
    WIDTH = 1
    HEIGHT = 1

    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.image = pygame.Surface([1, 400])
        self.image.fill(PINK)

        self.rect = self.image.get_rect()
        self.rect.x = -5
        self.rect.y = 0


class SecondStopBlock(StopBlock):
    """ This class represents the block subclass. """
    WIDTH = 1
    HEIGHT = 1

    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
        # This block will catch red blocks
        self.rect.x = 710
        self.rect.y = 0

