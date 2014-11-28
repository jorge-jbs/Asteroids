#Here elements get added to the general list


def asteroid(times=1):
    from src.elements.creation import Create
    from src.inits.levels.L1.__init__ import asteroids

    create = Create()

    for i in range(0, times):
        asteroids.append(1)
        asteroids[-1] = create.asteroid()

    return asteroids