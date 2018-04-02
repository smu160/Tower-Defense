# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 20:37:14 2018

@authors: Saveliy Yusufov and Michael Harley
"""
import random
import pygame
from button import Button
from cannon import Cannon
from cannon_display import Cannon_Display
from scoreboard import Scoreboard
from zombie import Zombie


class Game(object):
    FRAMES_PER_SEC = 60

    # The amount of zombies allowed past the perimeter before game over
    ZOMBIE_THRESH = 10

    def __init__(self, disp_width, disp_height):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.game_display = pygame.display.set_mode((disp_width, disp_height))
        pygame.display.set_caption("Tower Defense")
        self.background_img = pygame.image.load("grass.jpg").convert()
        self.scoreboard = Scoreboard()
        self.running = True
        self.herd_size = 10
        self.tick_count = 600 # Time to wait before the next wave of zombies

    def make_zombie_herd(self, num_of_zombies):
        """Creates a herd of zombies

        Creates a list of zombies generated in random positions on the screen
        start_x_pos for each zombie is a number in [-1000, 0)
        start_y_pos for each zombie is a random position along the y-axis

        Args:
            num_of_zombies: the amount of zombies to be generated in the herd
            height: the height of the display

        Returns: a sprite group of zombies
        """
        zombie_herd = pygame.sprite.Group()
        for _ in range(num_of_zombies):
            start_x = random.randint(-1050, -50)
            start_y = self.game_display.get_height() * random.uniform(0.1, 0.9)
            zombie_herd.add(Zombie(start_x, start_y))

        return zombie_herd

    def move_zombie_herd(self, zombie_group):
        """Moves a herd of zombies

        This function calls the zombie class move() function (with default delta)
        on a given zombie herd. If a zombie makes it past the perimeter, then it
        increments the zombies_past_perim counter, and removes the zombie from the
        zombie_group list

        Args:
            zombie_group: the zombie sprite group to be moved along the display
        """
        for zomb in zombie_group:
            if zomb.x > self.game_display.get_height():
                zombie_group.remove(zomb)
                self.scoreboard.score += 1

        zombie_group.update()
        zombie_group.draw(self.game_display)

    def display_warning(self, tick_counter):
        "Display a countdown on screen till the next wave, on the screen"
        text = pygame.font.Font(None, 50).render("Next wave in {}".format((tick_counter / 10)), True, (255, 255, 0))
        text_rect = text.get_rect()
        text_x = self.game_display.get_width() / 2 - text_rect.width / 2
        text_y = self.game_display.get_height() / 2 - text_rect.height / 2
        self.game_display.blit(text, [text_x, text_y])

    def display_game_over(self):
        "Display the Game Over screen with player/user stats"
        text = pygame.font.Font(None, 50).render("Game Over!", True, (255, 255, 0))
        text_rect = text.get_rect()
        text_x = self.game_display.get_width() / 2 - text_rect.width / 2
        text_y = self.game_display.get_height() / 2 - text_rect.height / 2
        wave_stats = pygame.font.Font(None, 36).render("You held off {} waves".format(self.scoreboard.wave), True, (255, 255, 0))
        kill_stats = pygame.font.Font(None, 36).render("You killed {} zombies".format(self.scoreboard.zombies_killed), True, (255, 255, 0))
        self.game_display.blit(wave_stats, [text_x-25, text_y+50])
        self.game_display.blit(kill_stats, [text_x-20, text_y+100])

    def run_game_loop(self):
        player_mouse_pos = [0, 0]
        button_clicked = False
        dragging = False
        game_over = False
        waves_allowed = True
        button = Button(15, 540, 50, 50)
        drag_cannon = Cannon([25, 552])
        cannon_display = Cannon_Display(self.scoreboard)
        cannon_sprite = pygame.sprite.Group(cannon_display)
        zombies_sprite = self.make_zombie_herd(self.herd_size)
        cannons = pygame.sprite.Group()
        score_sprite = pygame.sprite.Group(self.scoreboard)
        button_sprite = pygame.sprite.Group(button)


        # Game loop
        while self.running:

            # Event detection
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    button_clicked = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    player_mouse_pos[0] = event.pos[0]
                    player_mouse_pos[1] = event.pos[1]
                    if button_clicked and dragging and self.scoreboard.cannons > 0:
                        self.scoreboard.cannons -= 1
                        cannon = Cannon([player_mouse_pos[0]-45, player_mouse_pos[1]-45])
                        cannons.add(cannon)
                    button_clicked = False
                    dragging = False

            cannons.update()
            cannon_sprite.update()
            score_sprite.update()
            button_sprite.update("null")

            self.game_display.blit(self.background_img, (0, 0))

            # Get mouse position
            cannon_pos = pygame.mouse.get_pos()

            if 10 <= cannon_pos[0] <= 60 and 540 <= cannon_pos[1] <= 590 and button_clicked:
                button_sprite.update("shrink")
                dragging = True
            elif dragging:
                button_sprite.update("shrink")

            if button_clicked and dragging and self.scoreboard.cannons > 0:
                drag_cannon.display(self.game_display, cannon_pos[0]-45, cannon_pos[1]-45)

            # Check if the wave of zombies is empty, start the timer, don't allow waves
            # increment size of herd, and create a new herd to send as next wave
            if not zombies_sprite:
                waves_allowed = False
                self.herd_size += random.randint(3, 6)
                self.scoreboard.increment_wave()
                zombies_sprite = self.make_zombie_herd(self.herd_size)

            # If 10 secs passed since last wave, then release the next zombie wave
            if not waves_allowed:
                if self.tick_count == 600:
                    self.scoreboard.cannons += (self.scoreboard.cannon_cash // 50)
                    self.scoreboard.cannon_cash = (self.scoreboard.cannon_cash % 50)
                self.display_warning(self.tick_count)
                self.tick_count -= 1
                if self.tick_count == 0:
                    waves_allowed = True
                    self.tick_count = 600

            # If zombie waves are allowed to attack AND the game is not over,
            # then move the zombie wave across the screen
            if waves_allowed and not game_over:
                self.move_zombie_herd(zombies_sprite)

            if not game_over:
                cannons.draw(self.game_display)
                score_sprite.draw(self.game_display)
                button_sprite.draw(self.game_display)
                cannon_sprite.draw(self.game_display)

            if self.scoreboard.score >= self.ZOMBIE_THRESH:
                game_over = True

            # If game over is true, draw Game Over and display player's stats
            if game_over:
                self.display_game_over()

            # Check if zombie is within radius of any cannon
            if not game_over and waves_allowed:
                for cannon in cannons:
                    zombies_in_radius = pygame.sprite.spritecollide(cannon, zombies_sprite, False, collided=pygame.sprite.collide_circle)
                    if zombies_in_radius:
                        for zombie in zombies_in_radius:
                            cannon.shoot(zombie.rect.centerx, zombie.rect.centery, self.game_display)

                            # Now check for bullet - zombie collisions
                            hit_list = pygame.sprite.spritecollide(zombie, cannon.bullets, False)
                            if hit_list:
                                for bullet in hit_list:
                                    if zombie.health <= 0:
                                        self.scoreboard.zombies_killed += 1
                                        self.scoreboard.cannon_cash += 1
                                        zombies_sprite.remove(zombie)
                                    else:
                                        zombie.health -= 10
                                    cannon.bullets.remove(bullet)
                                cannon.bullets.empty()

            pygame.display.update()
            self.clock.tick(self.FRAMES_PER_SEC)
