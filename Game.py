#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 20:37:14 2018

@author:
"""
import pygame

WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 768

LIGHT_GREY = (240, 240, 240)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

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


def zombie(x, y):
    game_display.blit(zombie_img, (x, y))


x_tower = WINDOW_WIDTH * 0.85
y_tower = WINDOW_HEIGHT * 0.3

x_zombie = WINDOW_WIDTH * 0.01
y_zombie = WINDOW_HEIGHT * 0.5

crashed = False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    game_display.fill(LIGHT_GREY)
    tower(x_tower, y_tower)

    x_zombie += 5
    if x_zombie > 0 and x_zombie < x_tower:
        zombie(x_zombie, y_zombie)

    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()
