# imports
import pygame
import sys
from pygame.locals import *

import elements.building as build
import elements.deletion as delete

pygame.init()

# variables
windowSize = (256, 128)


# files
bg_if = "textures/elements/bg.jpg"
ast_if = "textures/elements/asteroid.png"


# initialization
screen = pygame.display.set_mode(windowSize, 0, 32)
background = pygame.image.load(bg_if).convert()
asteroid = pygame.image.load(ast_if).convert_alpha()


# building first asteroids
asteroids = []

build.asteroid(5)


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
    screen.blit(background, (0, 0))

    # create asteroids
    while len(asteroids) < 5:
        build.asteroid()
    for i in asteroids:
        screen.blit(asteroid, i["pos"])

    # update display
    pygame.display.update()