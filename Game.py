#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 20:37:14 2018

@author:
"""
import random
import time
import pygame
from Zombie import Zombie

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BLACK = (0, 0, 0)

pygame.init()
GAME_DISPLAY = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Tower Defense")
CLOCK = pygame.time.Clock()

zombies_past_perimeter = 0
background_img = pygame.image.load("grass_background.png").convert()


def make_zombie_herd(num_of_zombies, game_display):
    """Creates a herd of zombies

    Creates a list of zombies generated in random positions on the screen
    start_x_pos for each zombie is a number in [-1000, 0)
    start_y_pos for each zombie is a random position along the y-axis

    Args:
        num_of_zombies: the amount of zombies to be generated in the herd
        game_display: the pygame display intialized in the beginning
        WINDOW_HEIGHT: the height of the display

    Returns: a list of zombies
    """
    zombie_herd = list()
    for _ in range(0, num_of_zombies):
        start_x_pos = random.randint(-1000, 0)
        start_y_pos = WINDOW_HEIGHT * random.uniform(0.1, 0.9)
        zombie_herd.append(Zombie(start_x_pos, start_y_pos, game_display))

    return zombie_herd


def move_zombie_herd(zombie_group, zombies_past_perim):
    """Moves a herd of zombies

    Simply calls move() (with default delta) on
    all the zombies in a given zombie herd

    Args:
        zombie_group: the herd of zombies to be moved along the display
    """
    for zombie in zombie_group:

        # If a zombie makes it past the perimeter, then
        if zombie.x > WINDOW_WIDTH:
            zombies_past_perim += 1
            zombie_group.remove(zombie)
        zombie.move()


running = True
gates_of_hell_open = True
size_of_herd = 10
herd_of_zombies = make_zombie_herd(size_of_herd, GAME_DISPLAY)

# Time to begin waiting for next wave of zombies
begin_wait_time = 0

while running and zombies_past_perimeter < 100:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            print(mouse_position)

    GAME_DISPLAY.blit(background_img, (0, 0))

    # Check if the wave of zombies is empty
    if not herd_of_zombies:
        begin_wait_time = time.time()
        gates_of_hell_open = False
        size_of_herd += random.randint(3, 6)
        herd_of_zombies = make_zombie_herd(size_of_herd, GAME_DISPLAY)

    if not gates_of_hell_open:
        if time.time() - begin_wait_time >= 10:
            gates_of_hell_open = True

    # If zombie waves are allowed to attack then move them across the screen
    if gates_of_hell_open:
        move_zombie_herd(herd_of_zombies, zombies_past_perimeter)

    pygame.display.update()

    # Frames Per Second (FPS)
    # Will block execution until 1/60 seconds have passed
    # since the previous time clock.tick was called.
    CLOCK.tick(60)

pygame.display.quit()
quit()
