# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 22:43:27 2018

@authors: Saveliy Yusufov and Michael Harley
"""
import pygame

BLACK = (0, 0, 0)


class Bullet(pygame.sprite.Sprite):
    "Common base class for all bullets"

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([4, 2])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        
    def shoot(self, direction, enemy_x, enemy_y):
        if direction == "north":
            if enemy_x < self.rect.x:
                self.rect.x -= 3
                self.rect.y -= 3
            elif enemy_x > self.rect.x:
                self.rect.x += 3
                self.rect.y -= 3
            else:
                self.rect.y -= 3
        elif direction == "east":
            if enemy_y < self.rect.y:
                self.rect.x += 3
                self.rect.y -= 3
            elif enemy_y > self.rect.y:
                self.rect.x += 3
                self.rect.y += 3
            else:
                self.rect.x += 3
        elif direction == "west":
            if enemy_y < self.rect.x:
                self.rect.x -= 3
                self.rect.y -= 3
            elif enemy_y > self.rect.x:
                self.rect.x -= 3
                self.rect.y += 3
            else:
                self.rect.x -= 3
        if direction == "south":
            if enemy_x < self.rect.x:
                self.rect.x -= 3
                self.rect.y += 3
            elif enemy_x > self.rect.x:
                self.rect.x += 3
                self.rect.y += 3
            else:
                self.rect.y += 3
        
    def update(self, direction, enemy_x, enemy_y):
        """Overriden sprite function

        Args:
        """
        self.shoot(direction, enemy_x, enemy_y)
