# Here the asteroids get their random properties

from src.levels.properties import WINDOWS_SIZE


class Create:
    def __init__(self):
        pass

    def asteroid(self):
        import random
        uniform = random.uniform

        # position
        pos = [0, 0]
        pos[0] = uniform(0, WINDOWS_SIZE[0]+1)
        pos[1] = uniform(0, WINDOWS_SIZE[1]+1)

        # category
        category = 0  # randrange(0, 2) # asteroid form
                                        # la forma del asteroide

        # hardness
        hardness = uniform(1, 5)  # each levels of hardness makes the asteroid take more or less shots
                                    # to be destroyed

                                    # cada nivel de dureza hace que el asteroide
                                    # necesite mas o menos disparos para ser destruido o dividido

        # pieces
        pieces = uniform(2, 6)    # the number of little asteroids the main one will divide
                                    # el numero de pequenos asteroides en los que se dividira el grande

        # speed
        speed = [0, 0]
        speed[0] = uniform(-1, 1)
        speed[1] = uniform(-1, 1)

        # dictionary
        asteroid_properties = {"pos": pos,
                               "category": category,
                               "hardness": hardness,
                               "pieces": pieces,
                               "speed": speed}

        return asteroid_properties