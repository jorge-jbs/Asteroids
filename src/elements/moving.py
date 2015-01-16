"""
This module takes the main asteroids list and changes the position of all the asteroids, with their own speed.
"""


def asteroid(asteroids):
    for i in asteroids:
        i.rect.x += i.speed[0]
        i.rect.y += i.speed[1]

    return asteroids