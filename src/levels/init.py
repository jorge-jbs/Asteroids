"""
makes the variables needed to run the game
"""

import pygame
from src.levels.properties import WINDOWS_SIZE

display = pygame.display.set_mode(WINDOWS_SIZE, 0, 32)

levels = ['start', 'L1']
level = levels[0]