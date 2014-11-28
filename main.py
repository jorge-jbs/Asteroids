# imports
import pygame
import sys
from pygame.locals import *

import src.elements.building as build
import src.elements.deletion as delete
import src.elements.moving as move


pygame.init()

# variables
global windowSize
windowSize = (256, 128)
count = 0

# files
bg_if = "textures/elements/bg.jpg"
ast_if = "textures/elements/asteroid.png"


# initialization
display = pygame.display.set_mode(windowSize, 0, 32)
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



    # update display
    pygame.display.update()