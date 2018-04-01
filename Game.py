# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 20:37:14 2018

@authors: Saveliy Yusufov and Michael Harley
"""
import random
import time
import pygame
from cannon import Cannon
from scoreboard import Scoreboard
from Zombie import Zombie
from button import Button
from constants import *

pygame.init()
CLOCK = pygame.time.Clock()
GAME_DISPLAY = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Tower Defense")
background_img = pygame.image.load("grass_background.png").convert()


def make_zombie_herd(num_of_zombies):
    """Creates a herd of zombies

    Creates a list of zombies generated in random positions on the screen
    start_x_pos for each zombie is a number in [-1000, 0)
    start_y_pos for each zombie is a random position along the y-axis

    Args:
        num_of_zombies: the amount of zombies to be generated in the herd
        game_display: the pygame display intialized in the beginning
        WINDOW_HEIGHT: the height of the display

    Returns: a sprite group of zombies
    """
    zombie_herd = pygame.sprite.Group()
    for _ in range(num_of_zombies):
        start_x_pos = random.randint(-1050, -50)
        start_y_pos = WINDOW_HEIGHT * random.uniform(0.1, 0.9)
        zombie_herd.add(Zombie(start_x_pos, start_y_pos))

    return zombie_herd

def move_zombie_herd(zombie_group):
    """Moves a herd of zombies

    This function calls the zombie class move() function (with default delta)
    on a given zombie herd. If a zombie makes it past the perimeter, then it
    increments the zombies_past_perim counter, and removes the zombie from the
    zombie_group list

    Args:
        zombie_group: the herd of zombies to be moved along the display
    """
    for zomb in zombie_group:
        if zomb.x > WINDOW_WIDTH:
            zombie_group.remove(zomb)
            scoreboard.score += 1

    zombie_group.update()
    herd_of_zombies.draw(GAME_DISPLAY)
    
def display_warning(tick_counter):
    "Display a countdown on screen till the next wave, on the screen"
    text = pygame.font.Font(None, 50).render("Next wave in {}".format((tick_counter / 10)), True, (255, 255, 0))
    text_rect = text.get_rect()
    text_x = GAME_DISPLAY.get_width() / 2 - text_rect.width / 2
    text_y = GAME_DISPLAY.get_height() / 2 - text_rect.height / 2
    GAME_DISPLAY.blit(text, [text_x, text_y])

def display_game_over():
    "Display the Game Over screen with player/user stats"
    text = pygame.font.Font(None, 50).render("Game Over!", True, (255, 255, 0))
    text_rect = text.get_rect()
    text_x = GAME_DISPLAY.get_width() / 2 - text_rect.width / 2
    text_y = GAME_DISPLAY.get_height() / 2 - text_rect.height / 2
    wave_stats = pygame.font.Font(None, 36).render("You held off {} waves".format(scoreboard.wave), True, (255, 255, 0))
    kill_stats = pygame.font.Font(None, 36).render("You killed {} zombies".format(scoreboard.zombies_killed), True, (255, 255, 0))
    
    GAME_DISPLAY.blit(wave_stats, [text_x-25, text_y+50])
    GAME_DISPLAY.blit(kill_stats, [text_x-20, text_y+100])

running = True
gates_of_hell_open = True
size_of_herd = 10
herd_of_zombies = make_zombie_herd(size_of_herd)

# Time to begin waiting for next wave of zombies
tick_counter = 600

scoreboard = Scoreboard()
cannons = pygame.sprite.Group()
bullets = pygame.sprite.Group()
score_sprite = pygame.sprite.Group(scoreboard)
button = Button(10, 480, 100, 100)
button_sprite = pygame.sprite.Group(button)

x_mouse = 0
y_mouse = 0
firing_rate = 0
game_over = False
button_clicked = False
dragging = False
drag_cannon = Cannon(25, 552)

# Game loop
while running:

    # Event detection
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            button_clicked = True
        elif event.type == pygame.MOUSEBUTTONUP:
            x_mouse = event.pos[0]
            y_mouse = event.pos[1]
            if button_clicked and dragging and scoreboard.cannons > 0:
                scoreboard.cannons -= 1
                cannon = Cannon(x_mouse, y_mouse)
                cannons.add(cannon)
            button_clicked = False
            dragging = False

    cannons.update(GAME_DISPLAY)
    score_sprite.update()
    button_sprite.update("null")

    GAME_DISPLAY.blit(background_img, (0, 0))

    # Get mouse position
    cannon_pos = pygame.mouse.get_pos()
    cannon_pos_x = cannon_pos[0]
    cannon_pos_y = cannon_pos[1]

    if 10 <= cannon_pos_x <= 130 and 470 <= cannon_pos_y <= 590 and button_clicked:
        button_sprite.update("shrink")
        dragging = True
    elif dragging:
        button_sprite.update("shrink")

    if button_clicked and dragging and scoreboard.cannons > 0:
        drag_cannon.display(GAME_DISPLAY, cannon_pos_x, cannon_pos_y)


    # Check if the wave of zombies is empty, start the timer, don't allow waves
    # increment size of herd, and create a new herd to send as next wave
    if len(herd_of_zombies) == 0:
        begin_wait_time = time.time()
        gates_of_hell_open = False
        size_of_herd += random.randint(3, 6)
        scoreboard.increment_wave()
        herd_of_zombies = make_zombie_herd(size_of_herd)

    # If 10 secs passed since last wave, then release the next zombie wave
    if not gates_of_hell_open:
        if tick_counter == 600:
            print("about to add {} cannons".format(scoreboard.cannon_cash // 25))
            scoreboard.cannons += (scoreboard.cannon_cash // 25)
            print("about to add {} cannon cash".format(scoreboard.cannon_cash % 25))
            scoreboard.cannon_cash = (scoreboard.cannon_cash % 25)
        display_warning(tick_counter)
        tick_counter -= 1
        if tick_counter == 0:
            gates_of_hell_open = True
            tick_counter = 600

    # If zombie waves are allowed to attack AND the game is not over, then
    # move the zombie wave across the screen
    if gates_of_hell_open and not game_over:
        move_zombie_herd(herd_of_zombies)

    if not game_over:
        cannons.draw(GAME_DISPLAY)
        score_sprite.draw(GAME_DISPLAY)
        button_sprite.draw(GAME_DISPLAY)

    if scoreboard.score >= 100:
        game_over = True

    # If game over is true, draw Game Over and display player's stats
    if game_over:
        display_game_over()

    # Check if zombie is within radius of any cannon
    if not game_over:
        for cannon in cannons:
            zombies_in_radius = pygame.sprite.spritecollide(cannon, herd_of_zombies, False, collided=pygame.sprite.collide_circle)
            if zombies_in_radius:
                for zombie in zombies_in_radius:
                    cannon.shoot(zombie.rect.x, zombie.rect.y, GAME_DISPLAY)

                    # Now check for bullet - zombie collisions
                    hit_list = pygame.sprite.spritecollide(zombie, cannon.bullets, True)
                    if hit_list:
                        for bullet in hit_list:
                            bullets.remove(bullet)
                            zombie.health -= 10
                            if zombie.health <= 0:
                                scoreboard.zombies_killed += 1
                                scoreboard.cannon_cash += 1
                                herd_of_zombies.remove(zombie)
                        cannon.bullets.empty()

    pygame.display.update()

    # Will block execution until 1/60 secs have passed since the previous time
    # clock.tick was called.
    CLOCK.tick(FPS)

pygame.display.quit()
quit()
