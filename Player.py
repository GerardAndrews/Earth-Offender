import pygame

BLUE = (0,   0, 255)

class Player(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """

    # -- Methods
    def __init__(self, x, y):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()

        # Set height, width
        self.image = pygame.Surface([30, 30])
        self.image.fill(BLUE)
        self.image = pygame.image.load("player_sprite.png")
        # self.image_exp = pygame.image.load("explosion.png")

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # -- Attributes
        self.hit_points = 10
        # Set speed vector
        self.change_x = 0
        self.change_y = 0

    def change_speed(self, x, y):
        """ Change the speed of the player"""
        self.change_x += x
        self.change_y += y

    def update(self):
        """ Find a new position for the player"""
        self.rect.x += self.change_x
        self.rect.y += self.change_y

    def take_damage(self):
        self.hit_points -= 1
