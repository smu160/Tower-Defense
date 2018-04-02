# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 19:10:25 2018

@author: Saveliy Yusufov and Michael Harley
"""
import pygame
from game import Game

def main():
    "The main function of the entire Tower Defense game"
    game = Game(800, 600)
    game.run_game_loop()
    pygame.display.quit()
    quit()

if __name__ == '__main__':
    main()
