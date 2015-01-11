#Here elements get added to the general list


def asteroid(asteroids, times=1):
    from src.elements.creation import Create

    create = Create()

    for i in range(0, times):
        asteroids.append(1)
        asteroids[-1] = create.asteroid()

    return asteroids