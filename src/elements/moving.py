def asteroid(asteroids):
    for i in asteroids:
        i["pos"][0] += i["speed"][0]
        i["pos"][1] += i["speed"][1]

    return asteroids