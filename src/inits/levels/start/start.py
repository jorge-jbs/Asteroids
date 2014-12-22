import pygame, sys
pygame.init()
from pygame.locals import *

from src.inits.properties import WINDOWS_SIZE
from variables import *

a = 1

screen = pygame.display.set_mode(WINDOWS_SIZE, 0, 32)

bg = pygame.image.load(bg_i).convert()

title = pygame.image.load(title_i).convert_alpha()
title = pygame.transform.scale(title, (title.get_size()[0]*4, title.get_size()[1]*4))

play = pygame.image.load(play_i).convert_alpha()
play = pygame.transform.scale(play, (play.get_size()[0]*8, play.get_size()[1]*8))

# sizes
title_size = title.get_size()
play_size = play.get_size()

# positions
title_pos = (WINDOWS_SIZE[0]/2-title_size[0]/2, (WINDOWS_SIZE[1]/2-title_size[1]/2)-(WINDOWS_SIZE[1]/4))
play_pos = (WINDOWS_SIZE[0]/2-play_size[0]/2, (WINDOWS_SIZE[1]/2-play_size[1]/2)+50)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            mou_pos = pygame.mouse.get_pos()

            # check play
            if mou_pos[0] >= play_pos[0] and mou_pos[0] <= play_pos[0]+play_size[0] and mou_pos[1] >= play_pos[1] and mou_pos[1] <= play_pos[1]+play_size[1]:
                import src.inits.levels.L1.L1

    screen.blit(bg, (0, 0))
    screen.blit(title, title_pos)
    screen.blit(play, play_pos)
    pygame.display.update()



#screen.blit(title, (WINDOWS_SIZE[0]/2-title.get_size()[0]/2, WINDOWS_SIZE[1]/2-title.get_size()[1]/2))