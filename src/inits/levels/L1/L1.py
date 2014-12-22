# imports
import pygame, sys
from pygame.locals import *

from variables import *
from Asteroids import display

import src.elements.building as build
import src.elements.deletion as delete
import src.elements.moving as move

clock = pygame.time.Clock()


# images
background = pygame.image.load(bg_i).convert()
asteroid = pygame.image.load(ast_i).convert_alpha()

# building first asteroids
asteroids = []

for i in asteroids:
    print i
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
        if count <= len(asteroids):
            asteroids[count] = move.asteroid(i)

    pygame.display.update()

    clock.tick(60)