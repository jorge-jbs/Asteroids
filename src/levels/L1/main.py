# imports
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
    background = pygame.image.load(bg_i).convert()
    asteroid = pygame.image.load(ast_i).convert_alpha()

    global asteroids
    asteroids = []
    asteroids = build.asteroid(asteroids, 5)

    # main loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                asteroids = delete.asteroid(mouse_pos, asteroids)

        # building asteroids
        while len(asteroids) < 5:
            asteroids = build.asteroid(asteroids)

        # rendering
        display.blit(background, (0, 0))

        for i in asteroids:
            display.blit(asteroid, i["pos"])

        # moving
        asteroids = move.asteroid(asteroids)

        pygame.display.update()

        clock.tick(FRAME_RATE)