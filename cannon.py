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
        self.image = pygame.Surface([20, 15])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #self.bullets = pygame.sprite.Group()

    def draw(self, x, y):
        self.rect.x = x
        self.rect.y = y

    #def create_bullet(self):
        #bullet = Bullet(self.rect.x, self.rect.y - 25)
        #self.bullets.add(bullet)
        
    #def fire(self, game_display):
        #self.bullets.update()
        #self.bullets.draw(game_display)

    #def update(self, game_display):
     #   bullet = Bullet(self.rect.x - 25, self.rect.y)
      #  self.bullets.add(bullet)
       # self.bullets.update()
        #self.bullets.draw(game_display)
        


