"""
This is the first level of the game.
"""


import pygame
import sys
from pygame.locals import *

from src.levels.init import display
from src.levels.L1.variables import *
from src.levels.properties import FRAME_RATE

import src.elements.building as build
import src.elements.deletion as delete
import src.elements.moving as move


def l1():
    clock = pygame.time.Clock()

    # images
    background = pygame.image.load(bg_if).convert()

    # sprites
    asteroids_list = pygame.sprite.Group()
    asteroids = []
    asteroids = build.asteroid(asteroids, 5)

    for i in asteroids:
        asteroids_list.add(i)

    # main loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # deleting
            if event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                asteroids = delete.asteroid(mouse_pos, asteroids)

                for i in asteroids:
                    asteroids_list.add(i)

        # building asteroids
        while len(asteroids) < 5:
            asteroids = build.asteroid(asteroids)

            asteroids_list = pygame.sprite.Group()
            for i in asteroids:
                asteroids_list.add(i)

        # rendering
        display.blit(background, (0, 0))
        asteroids_list.draw(display)

        # moving
        asteroids_list = move.asteroid(asteroids_list)
        for i in asteroids:
            asteroids_list.add(i)

        pygame.display.update()

        clock.tick(FRAME_RATE)