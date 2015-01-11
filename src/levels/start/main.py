def start(level, levels):
    import pygame
    import sys

    from pygame.locals import QUIT, MOUSEBUTTONDOWN

    from src.levels.init import display

    from src.levels.properties import WINDOWS_SIZE
    from src.levels.start.variables import bg_i, title_i, play_i

    exit = False

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

    while exit is False:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                mou_pos = pygame.mouse.get_pos()

                # check play
                if mou_pos[0] >= play_pos[0] and mou_pos[0] <= play_pos[0]+play_size[0] and mou_pos[1] >= play_pos[1] and mou_pos[1] <= play_pos[1]+play_size[1]:
                    level = levels[1]
                    exit = True
        display.blit(bg, (0, 0))
        display.blit(title, title_pos)
        display.blit(play, play_pos)
        pygame.display.update()

    return level