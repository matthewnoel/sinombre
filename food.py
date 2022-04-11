import random

from positional import Positional


class Food(Positional):
    def __init__(self, world, x, y):
        Positional.__init__(self, world, x, y)

    def __repr__(self):
        return "\033[0;32;40m" + "O" + "\033[0;0m"

    def eat(self):
        seed_location = (
            random.randrange(0, self.world.size),
            random.randrange(0, self.world.size),
        )
        while not self.world.isLocationAccessible(seed_location[0], seed_location[1]):
            seed_location = (
                random.randrange(0, self.world.size),
                random.randrange(0, self.world.size),
            )
        self.world.plantFood(seed_location[0], seed_location[1])
        self.remove()
