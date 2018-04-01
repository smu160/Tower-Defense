# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 22:43:28 2018

@authors: Saveliy Yusufov and Michael Harley
"""
import pygame
from bullet import Bullet


class Cannon(pygame.sprite.Sprite):
    "Common base class for all cannons"

    cannon_count = 0

    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface([25, 25])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.radius = 75
        self.bullets = pygame.sprite.Group()

    def draw(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def shoot(self, dest_x, dest_y, game_display):
        bullet = Bullet(self.rect.centerx, self.rect.centery, dest_x+3, dest_y+3)
        self.bullets.add(bullet)
        self.bullets.update()
        self.bullets.draw(game_display)




