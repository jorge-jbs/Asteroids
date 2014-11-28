import pygame
from pygame.locals import *
pygame.init()

from variables.general import *
from src.inits.variables.files import *

display = pygame.display.set_mode(WINDOWS_SIZE, 0, 32)
background = pygame.image.load(BG).convert()
asteroid = pygame.image.load(AST).convert_alpha()