#Here elements get added to the general list


def asteroid(times=1):
    from src.elements.creation import Create
    from main import asteroids

    create = Create()

    for i in range(0, times):
        asteroids.append(1)
        asteroids[-1] = create.asteroid()

    return asteroids