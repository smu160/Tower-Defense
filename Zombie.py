# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 23:57:17 2018

@author:
"""

import pygame
from spritesheet_functions import SpriteSheet

WHITE = (255, 255, 255)


class Zombie(pygame.sprite.Sprite):
    "Common base class for all zombies"
    zombie_count = 0

    def __init__(self, x, y, game_display):
        super().__init__()
        self.x = x
        self.y = y
        self.game_display = game_display
        self.health = 100
        self.list_index = 0
        self.even_or_odd = "even"
        Zombie.zombie_count += 1

        spritesheet = SpriteSheet("Apple_Zombie.png")
        self.walking_frames_list = list()
        self.walking_frames_list.append(spritesheet.get_image(63, 65, 52, 63))
        self.walking_frames_list.append(spritesheet.get_image(126, 65, 52, 63))
        self.walking_frames_list.append(spritesheet.get_image(191, 65, 52, 63))
        self.walking_frames_list.append(spritesheet.get_image(255, 65, 52, 63))
        self.walking_frames_list.append(spritesheet.get_image(319, 65, 52, 63))
        self.walking_frames_list.append(spritesheet.get_image(384, 65, 52, 63))
        self.image = self.walking_frames_list[self.list_index]

    def move(self, DELTA=0.9):
        self.x += DELTA
        if self.even_or_odd == "even":
            self.list_index += 1
            self.image = self.walking_frames_list[self.list_index]
            self.even_or_odd = "odd"
        else:
            self.even_or_odd = "even"

        self.game_display.blit(self.image, (self.x, self.y))

        if self.list_index == len(self.walking_frames_list)-1:
            self.list_index = 0

    def displayCount(self):
        print("Total zombies {}".format(Zombie.zombie_count))

    def displayZombie(self):
        print("Coordinates: ({}, {})".format(self.x, self.y))

    def __del__(self):
        print("Zombie deleted!")
        self.zombie_count -= 1
