# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 23:57:17 2018

@authors: Saveliy Yusufov and Michael Harley
"""

import pygame
from spritesheet_functions import SpriteSheet

BLACK = (0, 0, 0)


class Zombie(pygame.sprite.Sprite):
    "Common base class for all zombies"
    zombie_count = 0

    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.health = 150
        self.list_index = 0
        self.even_or_odd = "even"
        Zombie.zombie_count += 1
        self.delta = 0.9

        spritesheet = SpriteSheet("Apple_Zombie.png")
        self.walking_frames_list = list()
        self.walking_frames_list.append(spritesheet.get_image(63, 65, 52, 63, "zombie"))
        self.walking_frames_list.append(spritesheet.get_image(126, 65, 52, 63, "zombie"))
        self.walking_frames_list.append(spritesheet.get_image(191, 65, 52, 63, "zombie"))
        self.walking_frames_list.append(spritesheet.get_image(255, 65, 52, 63, "zombie"))
        self.walking_frames_list.append(spritesheet.get_image(319, 65, 52, 63, "zombie"))
        self.walking_frames_list.append(spritesheet.get_image(384, 65, 52, 63, "zombie"))
        self.image = self.walking_frames_list[self.list_index]
        self.rect = self.image.get_rect()

    def update(self):
        """Move a zombie"""
        self.x += self.delta
        if self.even_or_odd == "even":
            self.list_index += 1
            self.image = self.walking_frames_list[self.list_index]
            self.rect.x = self.x
            self.rect.y = self.y
            self.even_or_odd = "odd"
        else:
            self.even_or_odd = "even"

        if self.list_index == len(self.walking_frames_list)-1:
            self.list_index = 0

    def displayCount(self):
        print("Total zombies {}".format(Zombie.zombie_count))

    def displayZombie(self):
        print("Coordinates: ({}, {})".format(self.x, self.y))

    def __del__(self):
        Zombie.zombie_count -= 1
