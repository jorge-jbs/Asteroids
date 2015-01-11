"""
This is the module that stores all the basic variables needed for the game.
"""


import pygame
from src.levels.properties import WINDOWS_SIZE

display = pygame.display.set_mode(WINDOWS_SIZE, 0, 32)

"""
Screens stores all the screens possible.
Screen stores the actual screen.
"""

screens = ['Start', 'L1']
screen = screens[0]