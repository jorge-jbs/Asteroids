"""
This is the main module that controls all the other modules.
"""


from src.levels.init import screen, screens

from src.levels.start.main import start
from src.levels.L1.main import l1


"""
Executes the current screen.
"""
if screen == screens[0]:
    screen = start(screen, screens)
if screen == screens[1]:
    l1()