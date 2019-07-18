import pygame

WHITE = (255, 255, 255)


class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.sound = pygame.mixer.Sound("Laser_Shoot.ogg")
        self.image = pygame.Surface([5, 5])
        self.image.fill(WHITE)

        self.rect = self.image.get_rect()

    def update(self):
        """ Move the bullet. """
        self.rect.x -= 7


class EnemyBullet(Bullet):
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()

    def update(self):

            self.rect.x += 6
