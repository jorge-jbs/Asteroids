"""
This modules has all the properties of the asteroid sprite.
"""


import pygame
import random

from src.levels.properties import WINDOWS_SIZE

uniform = random.uniform

ast_if = "textures/elements/asteroid.png"


class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        # position
        self.pos = [0, 0]
        self.pos[0] = uniform(0, WINDOWS_SIZE[0]+1)
        self.pos[1] = uniform(0, WINDOWS_SIZE[1]+1)

        # category
        self.category = 0  # randrange(0, 2)
        """
        Asteroid form
        """

        # hardness
        self.hardness = uniform(1, 5)
        """
        This is the number of times the asteroid needs to be fired to be destroyed.
        """

        # pieces
        self.pieces = uniform(2, 6)
        """
        This is the number of pieces the asteroid will be dived when is destroyed
        """

        # speed
        self.speed = [0, 0]

        self.speed[0] = uniform(-2, 2)
        while self.speed[0] <= 1 and self.speed[0] >= -1:
            self.speed[0] = uniform(-2, 2)

        self.speed[1] = uniform(-2, 2)
        while self.speed[1] <= 1 and self.speed[1] >= -1:
            self.speed[1] = uniform(-2, 2)
        """
        The number of pixels the asteroid moves each tick.
        """

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(ast_if).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect[0] = self.pos[0]
        self.rect[1] = self.pos[1]