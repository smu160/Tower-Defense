# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 21:30:13 2018

@author: Saveliy Yusufov and Michael Harley
"""
import pygame

class Scoreboard(pygame.sprite.Sprite):
    "Common base class for all scoreboards"

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # Score is the same as zombies past perimeter
        self.score = 0

        self.wave = 1

        self.font = pygame.font.SysFont("None", 30)

    def update(self):
        "Updates the game scoreboard"
        self.text = "zombies past perimeter: {}         wave: {}".format(self.score, self.wave)
        self.image = self.font.render(self.text, 1, (255, 255, 0))
        self.rect = self.image.get_rect()

    def increment_score(self):
        self.score += 1
        
    def increment_wave(self):
        self.wave += 1