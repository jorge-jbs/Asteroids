from src.levels.init import level, levels

from src.levels.start.main import start
from src.levels.L1.main import l1

if level == levels[0]:
    level = start(level, levels)
    print level
if level == levels[1]:
    l1()