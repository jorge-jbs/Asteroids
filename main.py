#imports
import pygame, sys
from pygame.locals import *
from new import new
pygame.init()

#variables
windowSize = (256, 128)

#files
bgif = "bg.jpg"
astif = "asteroid.png"

#initialization
screen = pygame.display.set_mode(windowSize, 0, 32)
background = pygame.image.load(bgif).convert()
asteroid = pygame.image.load(astif).convert_alpha()

    #initializing asteroids
def createAsteroid(times = 1):
    for i in range(0, times):
        asteroids.append(1)
        asteroids[-1] = new.asteroid()

new = new()

asteroids = []
createAsteroid(5)

print(asteroids)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(background, (0, 0))

    #create asteroids
    while len(asteroids) < 5:
        createAsteroid()
    for i in asteroids:
        screen.blit(asteroid, i["pos"])

    pygame.display.update()