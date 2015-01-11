"""
This module gets the properties of a new asteroid and adds them to the main asteroids list.
"""


from src.elements.creation import Create


def asteroid(asteroids, times=1):
    create = Create()

    for i in range(0, times):
        asteroids.append(1)
        asteroids[-1] = create.asteroid()

    return asteroids