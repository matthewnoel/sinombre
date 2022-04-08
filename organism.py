import random

from positional import Positional


def getRandomGenome():
    genome = ""
    genome += chr(65 + random.randrange(0, 6))
    return genome


class Organism(Positional):
    def __init__(self, world, x, y, genome=None):
        if genome is None:
            genome = getRandomGenome()
        self.genome = genome
        Positional.__init__(self, world, x, y)

    def __repr__(self):
        return self.genome

    def onTimeIncremented(self):
        if self.genome == "A":
            self.moveUp()
        elif self.genome == "B":
            self.moveRight()
        elif self.genome == "C":
            self.moveDown()
        elif self.genome == "D":
            self.moveLeft()
        elif self.genome == "E":
            self.moveRandom()
