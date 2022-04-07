from ast import Or
from organism import Organism


class Block:
    def __init__(self, x, y, atomic_number=0):
        self.location = (x, y)
        self.atomic_number = atomic_number
        self.occupant = None

    def __repr__(self):
        if self.occupant is not None:
            return str(self.occupant)
        return str(self.atomic_number)

    def incrementTime(self):
        return

    def spawnOrganism(self, genome=None):
        organism = None
        if genome is None:
            organism = Organism(self.location)
        else:
            organism = Organism(self.location, genome)
        self.occupant = organism
