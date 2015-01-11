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

asteroids = []
count = 0


def l1():
    clock = pygame.time.Clock()

    # images
    background = pygame.image.load(bg_i).convert()
    asteroid = pygame.image.load(ast_i).convert_alpha()

    # main loop
    while True:
        count = 0
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
            if count <= len(asteroids):
                asteroids[count] = move.asteroid(i)

        pygame.display.update()

        clock.tick(FRAME_RATE)