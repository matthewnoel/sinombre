import random

from organism import Organism


class World:
    def __init__(self, size):
        self.size = size
        self.position_relations = {}
        for x in range(size):
            for y in range(size):
                if random.randrange(1, 11) % 10 == 0:
                    self.spawnOrganism(x, y)

    def __repr__(self):
        retval = ""
        for x in range(self.size):
            for y in range(self.size):
                char = "_"
                positional = self.position_relations.get(
                    self.calculatePositionRelationIndex(x, y)
                )
                if positional is not None:
                    char = str(positional)
                retval += char
            retval += "\n"
        return retval

    def incrementTime(self):
        position_relations = self.position_relations.copy()
        for position in position_relations:
            self.position_relations[position].onTimeIncremented()

    def spawnOrganism(self, x, y, genome=None):
        organism = None
        if genome is None:
            organism = Organism(self, x, y)
        else:
            organism = Organism(self, x, y, genome)
        self.position_relations[self.calculatePositionRelationIndex(x, y)] = organism

    def calculatePositionRelationIndex(self, x, y):
        return (self.size * y) + x

    def isLocationAccessible(self, x, y):
        if x < 0 or y < 0 or x >= self.size or y >= self.size:
            return False
        if (
            self.position_relations.get(self.calculatePositionRelationIndex(x, y))
            is not None
        ):
            return False
        return True
