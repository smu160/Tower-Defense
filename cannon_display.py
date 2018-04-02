# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 21:30:13 2018

@author: Saveliy Yusufov and Michael Harley
"""
import pygame

YELLOW = (255, 255, 0)

class Cannon_Display(pygame.sprite.Sprite):
    "Common base class for all scoreboards"

    def __init__(self, scoreboard):
        pygame.sprite.Sprite.__init__(self)
        self.scoreboard = scoreboard
        self.font = pygame.font.SysFont("None", 30)
        self.text = "cannons available: {}".format(self.scoreboard.cannons)
        self.image = self.font.render(self.text, 1, YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100

    def update(self):
        "Updates the cannon display"
        self.text = "{}".format(self.scoreboard.cannons)
        self.image = self.font.render(self.text, 1, YELLOW)
        self.rect.x = 70
        self.rect.y = 575