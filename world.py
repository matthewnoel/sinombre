import random

from food import Food
from oasis import Oasis
from organism import Organism
from positional import Positional


class World:
    def __init__(self, size, life_odds=10, food_odds=20, oasis_odds=50):
        self.iteration = 0
        self.size = size
        self.position_relations = {}
        for x in range(size):
            for y in range(size):
                if random.randrange(0, oasis_odds) == 0:
                    self.createOasis(x, y)
                elif random.randrange(0, food_odds) == 0:
                    self.plantFood(x, y)
                elif random.randrange(0, life_odds) == 0:
                    self.spawnOrganism(x, y)

    def __repr__(self):
        retval = ""
        for x in range(self.size):
            for y in range(self.size):
                char = "\033[0;37;40m" + "." + "\033[0;0m"
                positional = self.position_relations.get(
                    self.calculatePositionRelationIndex(x, y)
                )
                if positional is not None:
                    char = str(positional)
                retval += char
            retval += "\n"
        return retval

    def calculatePositionRelationIndex(self, x, y):
        return (self.size * y) + x

    def incrementTime(self):
        retval = False
        position_relations = self.position_relations.copy()
        for position in position_relations:
            if type(position_relations[position]).__name__ == "Organism":
                retval = True
            position_relations[position].onTimeIncremented()
        if retval:
            self.iteration += 1
        return retval

    def spawnOrganism(self, x, y, genome=None):
        organism = None
        if genome is None:
            organism = Organism(self, x, y)
        else:
            organism = Organism(self, x, y, genome)
        self.position_relations[self.calculatePositionRelationIndex(x, y)] = organism

    def createOasis(self, x, y):
        self.position_relations[self.calculatePositionRelationIndex(x, y)] = Oasis(
            self, x, y
        )

    def plantFood(self, x, y):
        self.position_relations[self.calculatePositionRelationIndex(x, y)] = Food(
            self, x, y
        )

    def getPositionalAt(self, x, y):
        return self.position_relations.get(self.calculatePositionRelationIndex(x, y))

    def isLocationAccessible(self, x, y):
        if x < 0 or y < 0 or x >= self.size or y >= self.size:
            return False
        if self.getPositionalAt(x, y) is not None:
            return False
        return True

    def calculateOasisBoost(self, x, y):
        for transformation in Positional.transformations():
            if (
                type(
                    self.getPositionalAt(x + transformation[0], y + transformation[1])
                ).__name__
                == "Oasis"
            ):
                return self.getPositionalAt(
                    x + transformation[0], y + transformation[1]
                ).emittance
        return 0
