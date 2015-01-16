"""
This module gets the properties of a new asteroid and adds them to the main asteroids list.
"""


from src.elements.sprites import Asteroid


def asteroid(asteroids, times=1):
    for i in range(0, times):
        asteroids.append(1)
        asteroids[-1] = Asteroid()
    return asteroids