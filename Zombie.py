# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 23:57:17 2018

@author:
"""

import pygame
import random


class Zombie:
    "Common base class for all zombies"
    zombie_count = 0

    def __init__(self, x, y, game_display):
        self.x = x
        self.y = y
        self.game_display = game_display
        self.health = 100
        self.image = pygame.image.load("zombie.png")
        Zombie.zombie_count += 1

    def move(self):
        self.x += random.uniform(0.1, 0.9)
        self.game_display.blit(self.image, (self.x, self.y))

    def displayCount(self):
        print("Total zombies {}".format(Zombie.zombie_count))

    def displayZombie(self):
        print("Coordinates: ({}, {})".format(self.x, self.y))
