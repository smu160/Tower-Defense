#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 23:57:17 2018

@author:
"""

import pygame


class Zombie:
    "Common base class for all zombies"
    zombie_count = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        Zombie.zombie_count += 1

    def displayCount(self):
        print("Total zombies {}".format(Zombie.zombie_count))

    def displayZombie(self):
        print("Coordinates: ({}, {})".format(self.x, self.y))
