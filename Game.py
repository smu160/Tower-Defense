#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 20:37:14 2018

@author:
"""
import pygame
from Zombie import *

WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 768

LIGHT_GREY = (240, 240, 240)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

zombies_past_perimeter = 0

pygame.init()
game_display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Tower Defense")
clock = pygame.time.Clock()

tower_img = pygame.image.load("guard_tower.png")

# TODO: Remove white background from image somehow
zombie_img = pygame.image.load("zombie.png")


def tower(x, y):
    game_display.blit(tower_img, (x, y))


x_tower = WINDOW_WIDTH * 0.85
y_tower = WINDOW_HEIGHT * 0.3

x_zombie = WINDOW_WIDTH * 0.01
y_zombie = WINDOW_HEIGHT * 0.5

crashed = False

zombie_0 = Zombie(x_zombie, WINDOW_HEIGHT * 0.0, game_display)
zombie_1 = Zombie(x_zombie, WINDOW_HEIGHT * 0.1, game_display)
zombie_2 = Zombie(x_zombie, WINDOW_HEIGHT * 0.2, game_display)
zombie_3 = Zombie(x_zombie, WINDOW_HEIGHT * 0.3, game_display)
zombie_4 = Zombie(x_zombie, WINDOW_HEIGHT * 0.4, game_display)
zombie_5 = Zombie(x_zombie, WINDOW_HEIGHT * 0.5, game_display)
zombie_6 = Zombie(x_zombie, WINDOW_HEIGHT * 0.6, game_display)
zombie_7 = Zombie(x_zombie, WINDOW_HEIGHT * 0.7, game_display)
zombie_8 = Zombie(x_zombie, WINDOW_HEIGHT * 0.8, game_display)
zombie_9 = Zombie(x_zombie, WINDOW_HEIGHT * 0.9, game_display)
zombie_10 = Zombie(x_zombie, WINDOW_HEIGHT * 1.0, game_display)

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    game_display.fill(LIGHT_GREY)
    tower(x_tower, y_tower)

    zombie_0.move()
    zombie_1.move()
    zombie_2.move()
    zombie_3.move()
    zombie_4.move()
    zombie_5.move()
    zombie_6.move()
    zombie_7.move()
    zombie_8.move()
    zombie_9.move()
    zombie_10.move()
    # if x_zombie > 0 and x_zombie < x_tower:
    #    zombie(x_zombie, y_zombie)

    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()
