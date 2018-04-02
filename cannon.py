# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 22:43:28 2018

@authors: Saveliy Yusufov and Michael Harley
"""
import pygame
from bullet import Bullet
from spritesheet_functions import SpriteSheet

class Cannon(pygame.sprite.Sprite):
    "Common base class for all cannons"

    cannon_count = 0

    def __init__(self, coord_pair):
        super().__init__()
        spritesheet = SpriteSheet("towers.png")
        self.cannon_frames_list = list()
        self.cannon_frames_list.append(spritesheet.get_image(116, 0, 100, 107, "cannon")) # tower 1
        self.cannon_frames_list.append(spritesheet.get_image(227, 0, 100, 107, "cannon")) # tower 2
        self.cannon_frames_list.append(spritesheet.get_image(338, 0, 100, 107, "cannon")) # tower 3
        self.cannon_frames_list.append(spritesheet.get_image(449, 0, 100, 107, "cannon")) # tower 4
        self.cannon_frames_list.append(spritesheet.get_image(560, 0, 100, 107, "cannon")) # tower 5
        self.cannon_frames_list.append(spritesheet.get_image(671, 0, 100, 107, "cannon")) # tower 6
        self.cannon_frames_list.append(spritesheet.get_image(782, 0, 100, 107, "cannon")) # tower 7
        self.cannon_frames_list.append(spritesheet.get_image(893, 0, 100, 107, "cannon")) # tower 8
        self.cannon_frames_list.append(spritesheet.get_image(1004, 0, 100, 107, "cannon")) # tower 9
        self.cannon_frames_list.append(spritesheet.get_image(1115, 0, 100, 107, "cannon")) # tower 10
        self.cannon_frames_list.append(spritesheet.get_image(1226, 0, 100, 107, "cannon")) # tower 11
        self.cannon_frames_list.append(spritesheet.get_image(1337, 0, 100, 107, "cannon")) # tower 12
        self.cannon_frames_list.append(spritesheet.get_image(1448, 0, 100, 107, "cannon")) # tower 13
        self.cannon_frames_list.append(spritesheet.get_image(1559, 0, 100, 107, "cannon")) # tower 14
        self.cannon_frames_list.append(spritesheet.get_image(1670, 0, 100, 107, "cannon")) # tower 15
        self.cannon_frames_list.append(spritesheet.get_image(1781, 0, 100, 107, "cannon")) # tower 16
        self.list_index = 0
        self.image = self.cannon_frames_list[self.list_index]
        self.rect = self.image.get_rect()
        self.rect.x = coord_pair[0]
        self.rect.y = coord_pair[1]
        self.radius = 175
        self.bullets = pygame.sprite.Group()
        self.firing_rate = 0
        self.m = 0
        self.cannons = 5

    def update(self):
        """Move a zombie"""
        if self.m % 30 == 0:
            self.list_index += 1
            self.image = self.cannon_frames_list[self.list_index] 
        self.m += 1   

        if self.list_index == len(self.cannon_frames_list)-1:
            self.list_index = 0

    def draw(self, x, y):
        """Updates the bullet position

        Args:
            x: the new x coordinate where the bullet should be drawn
            y: the new y coordinate where the bullet should be drawn
        """
        self.rect.x = x
        self.rect.y = y

    def shoot(self, dest_x, dest_y, game_display):
        """Make the cannons shoot bullets

        Args:
            dest_x: the bullet's end point x coordinate
            dest_y: the bullet's end point y coordinate
            game_display: the game screen where all of the shooting is drawn
        """
        bullet = Bullet(self.rect.centerx, self.rect.centery, dest_x+3, dest_y+3)
        if self.firing_rate % 20 == 0:
            self.bullets.add(bullet)

        self.bullets.update()
        self.bullets.draw(game_display)
        self.firing_rate += 1

    def display(self, game_display, x, y):
        """

        Args:
            game_display: the game screen where all of the game play is drawn
            x: the x component of where the cannon picture should be blitted
            y: the y component of where the cannon picture should be blitted
        """
        game_display.blit(self.image, (x, y))

