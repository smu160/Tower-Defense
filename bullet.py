# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 22:43:27 2018

@authors: Saveliy Yusufov and Michael Harley
"""
import pygame

BLACK = (0, 0, 0)


class Bullet(pygame.sprite.Sprite):
    "Common base class for all bullets"

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([4, 2])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()

    def update(self):
        """Overriden sprite function

        Args:
        """
        self.rect.x -= 6
