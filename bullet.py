# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 22:43:27 2018

@authors: Saveliy Yusufov and Michael Harley
"""
import math
import pygame

class Bullet(pygame.sprite.Sprite):
    "Common base class for all bullets"

    BLACK = (0, 0, 0)

    def __init__(self, start_x, start_y, end_x, end_y):
        super().__init__()
        self.image = pygame.Surface([4, 4])
        #self.image.fill(self.BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = start_x
        self.rect.y = start_y

        # Because rect.x and rect.y are automatically converted to integers,
        # we need to create different variables that store the location as
        # floating point numbers in order to increase accuracy
        self.floating_point_x = start_x
        self.floating_point_y = start_y

        # Compute the angle in radians between the start points and end
        # points. This is the angle the bullet will travel along.
        x_diff = end_x - start_x
        y_diff = end_y - start_y
        angle = math.atan2(y_diff, x_diff)

        # Taking into account the angle, calculate our change_x
        # and change_y. Velocity is how fast the bullet travels.
        velocity = 15
        self.change_x = math.cos(angle) * velocity
        self.change_y = math.sin(angle) * velocity

        self.m = 0

    def update(self, color):
        "Move the bullet"
        # The floating point x and y hold our more accurate location.
        self.floating_point_y += self.change_y
        self.floating_point_x += self.change_x

        # The rect.x and rect.y are converted to integers.
        self.rect.y = int(self.floating_point_y)
        self.rect.x = int(self.floating_point_x)

        if color == "transparent":
            self.image.set_colorkey(self.BLACK)
        else:
            self.image.fill(color)
