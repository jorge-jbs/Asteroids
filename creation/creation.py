class create:
    #asteroid properties
    def asteroid(self, newAsteroid = 0):
        from random import randrange

        #position
        pos = [0, 0]
        pos[0] = randrange(0, 257)
        pos[1] = randrange(0, 129)

        #category
        category = randrange(0, 2) #la forma del asteroide

        #hardness
        hardness = randrange(1, 5) #cada nivel de dureza hace que el asteroide
                                   #se divida en mas o menos piezas cada vez que se le dispara

        #speed
        speed = [0, 0]
        speed[0] = randrange(-6, 6)
        speed[1] = randrange(-6, 6)

        newAsteroid = {"pos": pos,
                       "category": category,
                       "hardness": hardness,
                       "speed": speed}

        return newAsteroid