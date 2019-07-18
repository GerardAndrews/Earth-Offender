"""
Authors: Gerard Andrews & Liam Ollive

Version 1.1(Beta)

Functionality:
- The Player character is instantiated.
- A spawner is off screen that spawns enemy units, asteroids, and bosses
- Destroying enemies/asteroids/bosses add to score
- Miscellaneous Planet Sprite moves to the center on the screen based on score

How to Play:
- Space bar shoots projectiles and the
- Arrow keys allow you to move in all directions.
"""

import pygame
import random
import Player
import Stopblock
import Bullet
import Background

BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
RED = (255,   0,   0)
BLUE = (0,   0, 255)
PINK = (255, 0, 255)

totalScore = 0
text = "Start"
level = 1


class Enemy(pygame.sprite.Sprite):
    """ This class represents the block. """

    def __init__(self, color):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.Surface([20, 20])
        self.image.fill(color)
        self.image = pygame.image.load("enemy.png")

        self.rect = self.image.get_rect()

        # Set speed vector
        self.change_x = 0
        self.change_y = 0

        # Setup shooting projectile
        self.last = pygame.time.get_ticks()
        self.cd = 1000

    def update(self):
        """ Move the enemy. """
        self.rect.x += 1.5
        now = pygame.time.get_ticks()
        if now - self.last >= self.cd:
            self.last = now
            self.spawn_enemy_bullet()

        if level == 2:
            self.rect.x += 1.8
        if level == 3:
            self.rect.x += 2
        if level == 4:
            self.rect.x += 2.3
        if level == 5:
            self.rect.x += 2.5

    def spawn_enemy_bullet(self):
        bullet = Bullet.EnemyBullet()

        # Spawn a bullet based on the enemy transform
        bullet.rect.x = self.rect.x
        bullet.rect.y = self.rect.y

        # Add it to the sprites list
        all_sprites_list.add(bullet)
        enemy_bullet_list.add(bullet)


# class TitleSprite(pygame.sprite.Sprite):
#
#     def __init__(self, x, y):
#
#         super().__init__()
#
#         # Set height, width
#         self.image = pygame.Surface([30, 30])
#         self.image.fill(BLUE)
#         self.image = pygame.image.load("player_sprite.png")
#
#         self.rect = self.image.get_rect()
#         self.rect.x = x
#         self.rect.y = y


class Score(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # BUG: IMAGE IS GETTING IN FRONT OF SCORE.
        self.image = pygame.Surface([100, 40])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def display_feedback(self, screen):
        hp_str = "HP: " + str(player.hit_points)
        hp_font = pygame.font.SysFont('Calibri', 25, True, False)
        hp_text = hp_font.render(hp_str, True, WHITE)
        screen.blit(hp_text, [600, 35])

        score_str = "Score: " + str(totalScore)
        font = pygame.font.SysFont('Calibri', 25, True, False)
        game_text = font.render(score_str, True, WHITE)
        screen.blit(game_text, [10, 350])

        level_str = "Level: " + str(level)
        level_text = font.render(level_str, True, WHITE)
        screen.blit(level_text, [600, 10])

    def game_over(self, screen):
        game_over_str = "Mission Failed, We'll get'em next time"
        return_str = "Press enter to exit the game"
        font = pygame.font.SysFont('Calibri', 30, True, False)
        game_over_text = font.render(game_over_str, True, WHITE)
        return_text = font.render(return_str, True, WHITE)
        screen.blit(game_over_text, [130, 200])
        screen.blit(return_text, [180, 230])

    def win(self, screen):
        victory_str = "The Invasion has begun, you win!"
        return_str = "Press enter to exit the game"
        font = pygame.font.SysFont('Calibri', 30, True, False)
        victory_text = font.render(victory_str, True, WHITE)
        return_text = font.render(return_str, True, WHITE)
        screen.blit(victory_text, [130, 200])
        screen.blit(return_text, [180, 230])

    def title(self, screen):
        title_str = "Earth Offenders!"
        font = pygame.font.SysFont('Calibri', 50, True, False)
        title_text = font.render(title_str, True, BLUE)
        screen.blit(title_text, [150, 100])

    def subtitle(self, screen):
        subtitle_str = "Press ENTER to Start!"
        font = pygame.font.SysFont('Calibri', 25, True, False)
        subtitle_text = font.render(subtitle_str, True, BLACK)
        screen.blit(subtitle_text, [200, 150])

    def controlA(self, screen):
        controla_str = "-press space bar to fire at enemies-"
        font = pygame.font.SysFont('Calibri', 20, True, False)
        controla_text = font.render(controla_str, True, BLACK)
        screen.blit(controla_text, [175, 300])

    def controlB(self, screen):
        subtitle_str = "-use arrow keys to move-"
        font = pygame.font.SysFont('Calibri', 20, True, False)
        subtitle_text = font.render(subtitle_str, True, BLACK)
        screen.blit(subtitle_text, [200, 350])


class Planet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # STARS
        self.image = pygame.Surface([50, 50])
        self.image.fill(BLUE)
        self.image = pygame.image.load("earth.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 180

    def update(self):
        if totalScore >= 2000 and self.rect.x is not 100:
            self.rect.x = 100
        if totalScore >= 3500 and self.rect.x is not 200:
            self.rect.x = 200
        if totalScore >= 8000 and self.rect.x is not 300:
            self.rect.x = 300
        if totalScore >= 13000 and self.rect.x is not 380:
            self.rect.x = 380


class EnemyBoss(Enemy):
        def __init__(self, color):
            # Call the parent class (Enemy) constructor
            super().__init__(RED)
            self.hit_points = 20

            self.image = pygame.Surface([100, 100])
            self.image.fill(color)
            self.image = pygame.image.load("Boss.png")
            self.rect = self.image.get_rect()

            self.last = pygame.time.get_ticks()
            self.cd = 1000

        def update(self):
            # Move the enemy.
            # We want the boss to move up and down on the screen
            # and we need it to constantly fire projectiles
            # Have the boss get in front of the screen

            # The boss must stop moving forward
            if self.rect.x == -100:
                self.move_right()

            elif self.rect.x < 50 and self.rect.y > 5:
                self.move_diagnaldown()

            elif self.rect.x < 250 and self.rect.y > 5:
                self.move_diagnalup()

            elif self.rect.x < 400 and self.rect.y > 5:
                self.move_diagnaldown()

            elif self.rect.x < 500 and self.rect.y > 5:
                self.move_diagnalup()

            elif self.rect.x < 600 and self.rect.y > 5:
                self.move_diagnaldown()

            elif self.rect.x < 700 and self.rect.y > 5:
                self.move_diagnalup()

            now = pygame.time.get_ticks()
            if now - self.last >= self.cd:
                self.last = now
                self.spawn_enemy_bullet()

        # def move_up(self):
        #     self.rect.y = 1
        #
        # def move_down(self):
        #     self.rect.y += 1
        #
        # def move_left(self):
        #     self.rect.x -= 1

        def move_right(self):
            self.rect.x += 1

        def move_diagnalup(self):
            self.rect.x += 1
            self.rect.y -= 1

        def move_diagnaldown(self):
            self.rect.x += 1
            self.rect.y += 1

        def take_damage(self):
            self.hit_points -= 1

        def spawn_enemy_bullet(self):
            bullet = Bullet.EnemyBullet()

            # Spawn a bullet based on the enemy transform
            bullet.rect.x = self.rect.x
            bullet.rect.y = self.rect.y

            # Add it to the sprites list
            all_sprites_list.add(bullet)
            enemy_bullet_list.add(bullet)


class Spawner(pygame.sprite.Sprite):
    def __init__(self):
        # Call the parent class (Enemy) constructor
        super().__init__()
        self.image = pygame.Surface([1, 1])
        self.image.fill(RED)
        self.rect = self.image.get_rect()

        self.rect.x = -10
        self.rect.y = 200

        self.last = pygame.time.get_ticks()
        self.cd = 1500

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last >= self.cd and len(boss_list) == 0:
            self.spawn()
            if totalScore >= 2000:
                self.asteroid_spawn()
            self.last = now

        # Scale Difficulty
        if totalScore >= 2000:
            self.cd = 1200

        if totalScore >= 4000:
            self.cd = 900

        if totalScore >= 8000:
            self.cd = 800

        if totalScore >= 10000:
            self.cd = 775

        if totalScore >= 12000:
            self.cd = 750

        # Spawn boss fight at specific points
        if totalScore == 1500 and len(boss_list) == 0 \
                or totalScore == 3000 and len(boss_list) == 0 \
                or totalScore == 4500 and len(boss_list) == 0 \
                or totalScore == 6000 and len(boss_list) == 0 \
                or totalScore == 7500 and len(boss_list) == 0 \
                or totalScore == 9000 and len(boss_list) == 0 \
                or totalScore == 10500 and len(boss_list) == 0:

            self.boss_spawn()

    def spawn(self):
        for _ in range(1):
            enemy = Enemy(RED)

        # Set a random location for the enemy
            enemy.rect.x = random.randrange(-100, -40, 1)
            enemy.rect.y = random.randrange(screen_height - 40)

            # Add the enemy to the list of objects
            enemy_list.add(enemy)
            all_sprites_list.add(enemy)

    def boss_spawn(self):
        for _ in range(1):
            boss = EnemyBoss(RED)

            # Sets location for the boss
            boss.rect.x = -100
            boss.rect.y = 150

            # Add the boss to the list of objects
            boss_list.add(boss)
            all_sprites_list.add(boss)

    def asteroid_spawn(self):
        for _ in range(1):
            asteroid = Asteroid(RED)

            # Set a random location for the block
            asteroid.rect.x = random.randrange(-100, -40, 1)
            asteroid.rect.y = random.randrange(screen_height - 40)

            # Add the enemy to the list of objects
            asteroid_list.add(asteroid)
            all_sprites_list.add(asteroid)


class Asteroid(pygame.sprite.Sprite):
    def __init__(self, color):
        # Call the parent class (Enemy) constructor
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(color)
        self.image = pygame.image.load("asteroid.png").convert()
        self.rect = self.image.get_rect()

        # Set speed vector
        self.change_x = 0
        self.change_y = 0

    def update(self):
        """ Move the enemy. """
        self.rect.x += 2

        # Scale Difficulty
        if level == 2:
            self.rect.x += 2.2
        if level == 3:
            self.rect.x += 2.5
        if level == 4:
            self.rect.x += 2.8
        if level == 5:
            self.rect.x += 3


# Now it's time to draw stars in the background
def draw_background():
    for _ in range(30):
        star = Background.Background()

        # Set a random location for the block
        star.rect.x = random.randrange(5, screen_width, 1)
        star.rect.y = random.randrange(screen_height - 10)

        # Spawn stars on the screen
        all_sprites_list.add(star)


# Call this function so the PyGame library can initialize itself
pygame.init()

# Create an 700x400 sized screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
newrange = 5
p = True

# --- Sprite lists

# This is a list of every sprite. All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()

# List of each block in the game
enemy_list = pygame.sprite.Group()
asteroid_list = pygame.sprite.Group()

# List of each bullet
bullet_list = pygame.sprite.Group()

# List of bosses
boss_list = pygame.sprite.Group()

# List of each bullet
enemy_bullet_list = pygame.sprite.Group()

# List of each player
player_list = pygame.sprite.Group()

# Set the title of the window
pygame.display.set_caption('Test')

# Create the player object
player = Player.Player(600, 200)
player_list.add(player)
all_sprites_list.add(player)

# Create an instance of the stop-block called backstop
backstop = Stopblock.StopBlock()
all_sprites_list.add(backstop)

backstop_two = Stopblock.SecondStopBlock()
all_sprites_list.add(backstop_two)

# Create a spawner
spawn_point = Spawner()
all_sprites_list.add(spawn_point)

score = Score(-10, 0)
all_sprites_list.add(score)

# Draw Planet Earth
planet = Planet()
all_sprites_list.add(planet)

# Draw Stars
draw_background()

clock = pygame.time.Clock()
time_elapsed_since_last_action = 0

total = 0
done = False
intro = True

# Splash Screen
while intro:

    screen.fill(WHITE)

    # Displays the text on the splash screen
    score.title(screen)
    score.subtitle(screen)
    score.controlA(screen)
    score.controlB(screen)
    # TitleSprite(300, 50)

    # Press enter on splash screen to go to game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # Press enter to start game
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:

                # loads music when enter is pressed
                pygame.mixer.music.load('spaec.mp3')

                # sets volume, range 0.0 to 1.0
                pygame.mixer.music.set_volume(0.3)

                # plays loaded music track
                pygame.mixer.music.play(-1)

                # ends intro screen
                intro = False

        # Flip screen
        pygame.display.flip()

        # Pause
        clock.tick(60)

# Game
while not done and not intro:

    # Display the score
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # Set the speed based on the key pressed
        elif event.type == pygame.KEYDOWN and len(player_list) is not 0:
            if event.key == pygame.K_LEFT:
                player.change_speed(-3, 0)
            elif event.key == pygame.K_RIGHT:
                player.change_speed(3, 0)
            elif event.key == pygame.K_UP:
                player.change_speed(0, -3)
            elif event.key == pygame.K_DOWN:
                player.change_speed(0, 3)

            # Fires bullet when space is pressed
            elif event.key == pygame.K_SPACE and len(player_list) is not 0:
                # Fire a bullet if the user clicks the space button
                bullet = Bullet.Bullet()
                # plays bullet sound
                bullet.sound.play()
                # Set the bullet so it is where the player is
                bullet.rect.x = player.rect.x
                bullet.rect.y = player.rect.y
                # Add the bullet to the lists
                all_sprites_list.add(bullet)
                bullet_list.add(bullet)

        # Reset speed when key goes up
        elif event.type == pygame.KEYUP and len(player_list) is not 0:
            if event.key == pygame.K_LEFT:
                player.change_speed(3, 0)
            elif event.key == pygame.K_RIGHT:
                player.change_speed(-3, 0)
            elif event.key == pygame.K_UP:
                player.change_speed(0, 3)
            elif event.key == pygame.K_DOWN:
                player.change_speed(0, -3)

        # Let the game exit when defeat happens
        elif event.type == pygame.KEYDOWN and len(player_list) is 0:
            if event.key == pygame.K_RETURN:
                # intro = True
                done = True

        # Let the game exit when Victory
        if event.type == pygame.KEYDOWN and planet.rect.x >= 380:
            if event.key == pygame.K_RETURN:
                # intro = True
                done = True

    # This actually moves the player block based on the current speed
    player.update()

    # We want to make sure is is the only condition on which the player dies
    if player.hit_points <= 0 and p is True:
        # player.image = player.image_exp
        p = False
        player_list.remove(player)
        all_sprites_list.remove(player)
        player_effect = pygame.mixer.Sound('player-explosion.wav')
        player_effect.play(0)

    # If the player gets near the right side, shift the player back
    if player.rect.right > screen_width:
        player.rect.right = screen_width

    # If the player gets near the left side, shift the player back
    if player.rect.left < 0:
        player.rect.left = 0

    # If the player gets near the bottom, shift the player back
    if player.rect.bottom > screen_height:
        player.rect.bottom = screen_height

    # If the player gets near the top, shift the player back
    if player.rect.top < 0:
        player.rect.top = 0

    # --- Game logic

    # Call the update() method on all the sprites
    all_sprites_list.update()

    if totalScore >= 2000:
        level = 2
    if totalScore >= 4000:
        level = 3
    if totalScore >= 8000:
        level = 4
    if totalScore >= 12000:
        level = 5

    # Make sure the backstop wipes out enemy bullets off screen
    e_bullet_hit_list = pygame.sprite.spritecollide(
        backstop_two, enemy_bullet_list, True)

    # Make sure the backstop wipes out enemies off-screen
    enemy_collide_list = pygame.sprite.spritecollide(
        backstop_two, enemy_list, True)

    # Make sure the backstop wipes out asteroids off-screen
    asteroid_collide_list = pygame.sprite.spritecollide(
        backstop_two, asteroid_list, True)

    # Make sure the backstop wipes out Boss off-screen

    # Calculate mechanics for each bullet
    for bullet in bullet_list:

        # See if it hit a block
        block_hit_list = pygame.sprite.spritecollide(bullet, enemy_list, True)
        asteroid_hit_list = pygame.sprite.spritecollide(
            bullet, asteroid_list, True)

        boss_hit_list = pygame.sprite.spritecollide(bullet, boss_list, False)

        for boss in boss_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            boss.take_damage()
            if boss.hit_points <= 0:
                effect = pygame.mixer.Sound('boss-explosion.wav')
                effect.play()
                all_sprites_list.remove(boss)
                boss_list.remove(boss)
                totalScore += 1000

        # For each block hit, remove the bullet and add to the score
        for enemy in block_hit_list:

            effect = pygame.mixer.Sound('enemy-explosion.wav')
            effect.play()
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            totalScore += 25

        # For each asteroid hit, remove the bullet and add to the score
        for asteroid in asteroid_hit_list:

            effect = pygame.mixer.Sound('enemy-explosion.wav')
            effect.play()
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            totalScore += 50

    bullet_hit_list = pygame.sprite.spritecollide(backstop, bullet_list, True)

    for boss in boss_list:
        boss_game_over = pygame.sprite.spritecollide(
            boss, player_list, False)
        for player in boss_game_over:
            player.take_damage()

    for enemy in enemy_list:

        # Kill Player
        enemy_game_over = pygame.sprite.spritecollide(
            enemy, player_list, False)

        for player in enemy_game_over:
            player.take_damage()

    for asteroid in asteroid_list:

        # Kill Player
        asteroid_game_over = pygame.sprite.spritecollide(
            asteroid, player_list, False)

        for player in asteroid_game_over:
            player.take_damage()

    for bullet in enemy_bullet_list:
        enemy_bullet_collide_hit_list = pygame.sprite.spritecollide(
            bullet, player_list, False)

        for player in enemy_bullet_collide_hit_list:
            player.take_damage()
            enemy_bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)

    # -- Draw everything

    # Clear screen
    screen.fill(BLACK)

    # Show the score
    score.display_feedback(screen)

    if len(player_list) == 0:
        score.game_over(screen)

    if planet.rect.x >= 380:
        score.win(screen)

    # Draw sprites
    all_sprites_list.draw(screen)
    pygame.draw.rect(screen, BLUE, [20, 425, 150, 50], 0)
    # Flip screen
    pygame.display.flip()

    # Pause
    clock.tick(60)

pygame.quit()
