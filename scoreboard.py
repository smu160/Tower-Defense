# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 21:30:13 2018

@author: Saveliy Yusufov and Michael Harley
"""
import pygame

YELLOW = (255, 255, 0)

class Scoreboard(pygame.sprite.Sprite):
    "Common base class for all scoreboards"

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.score = 0 # Score is the same as zombies past perimeter
        self.wave = 1
        self.cannon_cash = 0
        self.total_kills = 0
        self.zombies_killed = 0
        self.font = pygame.font.SysFont("None", 30)
        self.text = "zombies past perimeter: {}".format(self.score) 
        self.text += " | wave: {}".format(self.wave)
        self.text += " | zombies killed: {}".format(self.zombies_killed)
        self.image = self.font.render(self.text, 1, YELLOW)
        self.rect = self.image.get_rect()
        self.cannons = 3

    def update(self):
        "Updates the game scoreboard"
        self.text = "zombies past perimeter: {}".format(self.score) 
        self.text += " | wave: {}".format(self.wave)
        self.text += " | zombies killed: {}".format(self.zombies_killed)
        self.image = self.font.render(self.text, 1, YELLOW)
        self.rect = self.image.get_rect()
        

    def increment_score(self):
        "Increments the score (the zombies paster the defense perimeter)"
        self.score += 1

    def increment_wave(self):
        "Increments the amount of waves of zombies count"
        self.wave += 1

    def compute_scores(self):
        "Increments the amount of zombies the player has killed"
        self.total_kills += self.zombies_killed
        self.cannon_cash += self.zombies_killed
        print("zombies_killed: {} total kills: {} cannon cash: {}".format(self.zombies_killed, self.total_kills, self.cannon_cash))
        self.zombies_killed = 0

    def increment_cannons_available(self):
        "Increments the amount of cannons the player has available"
        self.cannons += (self.cannon_cash // 25)
        self.cannon_cash += (self.cannon_cash % 25)