#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 20:37:14 2018

@author:
"""
import pygame
import random
from Zombie import Zombie

WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 768

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

zombies_past_perimeter = 0

pygame.init()
game_display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Tower Defense")
clock = pygame.time.Clock()

background_img = pygame.image.load("grass_background.png")

tower_img = pygame.image.load("guard_tower.png").convert()
tower_img.set_colorkey((255, 255, 255))


def tower(x, y):
    game_display.blit(tower_img, (x, y))


x_tower = WINDOW_WIDTH * 0.85
y_tower = WINDOW_HEIGHT * 0.3


def make_zombie_herd(num_of_zombies, game_display, WINDOW_HEIGHT):
    """Creates a herd of zombies

    Creates a list of zombies generated in random positions on the screen
    start_x_pos for each zombie is a number in [-100, 0)
    start_y_pos for each zombie is a random position along the y-axis

    Args:
        num_of_zombies: the amount of zombies to be generated in the herd
        game_display: the pygame display intialized in the beginning
        WINDOW_HEIGHT: the height of the display

    Returns: a list of zombies
    """
    zombie_herd = list()
    for _ in range(0, num_of_zombies):
        start_x_pos = random.randint(-100, 0)
        start_y_pos = WINDOW_HEIGHT * random.uniform(0.1, 0.9)
        zombie_herd.append(Zombie(start_x_pos, start_y_pos, game_display))

    return zombie_herd


def move_zombie_herd(zombie_herd):
    """Moves a herd of zombies

    Simply calls move() (with default delta) on
    all the zombies in a given zombie herd

    Args:
        zombie_herd: the herd of zombies to be moved along the display
    """
    for zombie in zombie_herd:
        zombie.move()


zombie_herd = make_zombie_herd(500, game_display, WINDOW_HEIGHT)

crashed = False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    game_display.blit(background_img, (0, 0))
    # tower(x_tower, y_tower)

    move_zombie_herd(zombie_herd)

    pygame.display.update()

    # Frames Per Second (FPS)
    clock.tick(60)

pygame.quit()
quit()
