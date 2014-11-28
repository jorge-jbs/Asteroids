# imports
import pygame
import sys
from pygame.locals import *

from src.inits.init import *
from src.inits.levels.L1.__init__ import *

import src.elements.building as build
import src.elements.deletion as delete
import src.elements.moving as move

pygame.init()


def l1():
    # building first asteroids
    count = 0

    # main loop
    while True:
        # exit
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                delete.asteroid()

        # background
        display.blit(background, (0, 0))

        # create asteroids
        while len(asteroids) < 5:
            build.asteroid()

        for i in asteroids:
            display.blit(asteroid, i["pos"])

        for i in asteroids:
            if count >= len(asteroids):
                break
            asteroids[count] = move.asteroid(i)

        pygame.display.update()