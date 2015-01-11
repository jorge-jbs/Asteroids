"""
This module contains all the properties that an asteroid has.
"""


import random
uniform = random.uniform

from src.levels.properties import WINDOWS_SIZE


class Create:
    def __init__(self):
        pass

    def asteroid(self):

        # position
        pos = [0, 0]
        pos[0] = uniform(0, WINDOWS_SIZE[0]+1)
        pos[1] = uniform(0, WINDOWS_SIZE[1]+1)

        # category
        category = 0  # randrange(0, 2)
        """
        Asteroid form
        """

        # hardness
        hardness = uniform(1, 5)
        """
        This is the number of times the asteroid needs to be fired to be destroyed.
        """

        # pieces
        pieces = uniform(2, 6)
        """
        This is the number of pieces the asteroid will be dived when is destroyed
        """

        # speed
        speed = [0, 0]
        speed[0] = uniform(-1, 1)
        speed[1] = uniform(-1, 1)
        """
        The number of pixels the asteroid moves each tick.
        """

        # dictionary
        asteroid_properties = {"pos": pos,
                               "category": category,
                               "hardness": hardness,
                               "pieces": pieces,
                               "speed": speed}

        return asteroid_properties