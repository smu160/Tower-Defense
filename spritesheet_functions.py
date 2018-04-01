# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 18:58:47 2018

@authors: Saveliy Yusufov and Michael Harley
"""
import pygame


class SpriteSheet(object):
    """ Class used to grab images out of a sprite sheet. """

    def __init__(self, file_name):
        """ Constructor. Pass in the file name of the sprite sheet. """

        # Load the sprite sheet.
        self.sprite_sheet = pygame.image.load(file_name).convert()

    def get_image(self, x, y, width, height, object_type):
        """
            Grab a single image out of a larger spritesheet
            Pass in the x, y location of the sprite
            and the width and height of the sprite.
        """

        # Create a new blank image
        image = pygame.Surface([width, height]).convert()

        # Copy the sprite from the large sheet onto the smaller image
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        # Assuming white works as the transparent color
        if object_type == "zombie":
            image.set_colorkey((255, 255, 255))
        elif object_type == "cannon":
            image.set_colorkey((0, 0, 0))

        # Return the image
        return image
