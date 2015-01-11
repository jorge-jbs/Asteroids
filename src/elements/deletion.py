#Here elements get deleted


def asteroid():
    import pygame
    from math import sqrt
    from src.levels.L1.main import asteroids, count

    mouse_pos = pygame.mouse.get_pos()

    for i in asteroids:
        distance = sqrt((mouse_pos[0] - (i["pos"][0]+11.5))**2 + (mouse_pos[1] - (i["pos"][1]+11.5))**2)
        if distance <= 11.5:
            del asteroids[count]
        count += 1