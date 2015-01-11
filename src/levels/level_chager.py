"""
changes between levels:
levels = stores all of the  game levels
level_pos = stores the position of the level ,that is currently playing, inside the levels list
level = stores the level that is currently playing
"""


levels = ['start', 'L1']
level_pos = 0
level = levels[level_pos]


def change_level(n):
    """
    sets level_pos to the argument
    and then refreshes level
    """

    level_pos = n
    level = levels[level_pos]