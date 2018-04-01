# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 22:43:28 2018

@authors: Saveliy Yusufov and Michael Harley
"""
import pygame
from bullet import Bullet
from spritesheet_functions import SpriteSheet

class Cannon(pygame.sprite.Sprite):
    "Common base class for all cannons"

    cannon_count = 0

    def __init__(self, x, y):
        super().__init__()
        sprite_sheet = SpriteSheet("wallturret.png")
        self.image = sprite_sheet.get_image(12, 50, 20, 20)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.radius = 75
        self.bullets = pygame.sprite.Group()
        self.firing_rate = 0

    def draw(self, x, y):
        """Updates the bullet position

        Args:
            x: the new x coordinate where the bullet should be drawn
            y: the new y coordinate where the bullet should be drawn
        """
        self.rect.x = x
        self.rect.y = y

    def shoot(self, dest_x, dest_y, game_display):
        """Make the cannons shoot bullets

        Args:
            dest_x: the bullet's end point x coordinate
            dest_y: the bullet's end point y coordinate
            game_display: the game screen where all of the shooting is drawn
        """
        bullet = Bullet(self.rect.centerx, self.rect.centery, dest_x+3, dest_y+3)
        if self.firing_rate % 15 == 0:
            self.bullets.add(bullet)

        self.bullets.update()
        self.bullets.draw(game_display)
        self.firing_rate += 1

    def display(self, game_display, x, y):
        """

        Args:
            game_display: the game screen where all of the game play is drawn
            x: the x component of where the cannon picture should be blitted
            y: the y component of where the cannon picture should be blitted
        """
        game_display.blit(self.image, (x, y))

