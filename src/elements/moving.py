def asteroid(moved):
    moved["pos"][0] += moved["speed"][0]
    moved["pos"][1] += moved["speed"][1]

    return moved