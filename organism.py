import random

from monomer import Monomer
from positional import Positional


def getRandomGenome():
    return [
        Monomer(10),
        Monomer(10),
        Monomer(10),
        Monomer(10),
        Monomer(10),
        Monomer(10),
        Monomer(10),
        Monomer(10),
        Monomer(10),
        Monomer(10),
    ]


class Organism(Positional):
    def __init__(self, world, x, y, genome=None):
        if genome is None:
            genome = getRandomGenome()
        self.genome = genome
        self.health = 20
        self.initial_health = 30
        self.preferred_mate = None
        self.active_monomer = 0
        Positional.__init__(self, world, x, y)

    def __repr__(self):
        dict = {}
        for monmer in self.genome:
            if not monmer.value in dict:
                dict[monmer.value] = 1
            else:
                dict[monmer.value] += 1
        value = self.genome[0]
        max_count = 0
        for key in dict:
            if dict[key] > max_count:
                value = key
                max_count = dict[key]
        bg = 40 + int(value * 7 / 10)
        fg = 30
        if bg == 40 or bg == 44:
            fg = 37
        return "\033[0;" + str(fg) + ";" + str(bg) + "m" + "X" + "\033[0;0m"

    def _handleMovement(self):
        value = self.genome[self.active_monomer].value
        if value == 0:
            self.moveNorth()
        elif value == 1:
            self.moveNorthEast()
        elif value == 2:
            self.moveEast()
        elif value == 3:
            self.moveSouthEast()
        elif value == 4:
            self.moveSouth()
        elif value == 5:
            self.moveSouthWest()
        elif value == 6:
            self.moveWest()
        elif value == 7:
            self.moveNorthWest()
        elif value == 8:
            self.moveRandom()

    def _tryEating(self):
        retval = 0

        for transformation in Positional.transformations():
            positional = self.world.getPositionalAt(
                self.x + transformation[0], self.y + transformation[1]
            )
            if positional is not None and type(positional).__name__ == "Food":
                positional.eat()
                retval += 2

        return retval

    def _handleHealth(self):
        self.health -= 1
        self.health += self.world.calculateOasisBoost(self.x, self.y)
        self.health += self._tryEating()
        if self.health <= 0:
            self.remove()

    def _birthChild(self, other_genome):
        genome = []
        for i in range(len(self.genome)):
            inherited_monomer = None
            if random.randrange(0, 2) == 0:
                inherited_monomer = Monomer(self.genome[i].range, self.genome[i].value)
            else:
                inherited_monomer = Monomer(
                    other_genome[i].range, other_genome[i].value
                )

            if (
                random.randrange(
                    0,
                    max(
                        2,
                        int((1 - self.health / self.initial_health) * self.health),
                    ),
                )
                == 0
            ):
                inherited_monomer.mutate()
            genome.append(inherited_monomer)

        for transformation in Positional.transformations():
            if (
                self.world.getPositionalAt(
                    self.x + transformation[0], self.y + transformation[1]
                )
                is None
            ):
                self.world.spawnOrganism(
                    self.x + transformation[0], self.y + transformation[1], genome
                )

    def _handleReproduction(self):
        for transformation in Positional.transformations():
            positional = self.world.getPositionalAt(
                self.x + transformation[0], self.y + transformation[1]
            )
            if positional is not None and type(positional).__name__ == "Organism":
                if random.randrange(0, 200) == 0:
                    self.preferred_mate = (
                        self.x + transformation[0],
                        self.y + transformation[1],
                    )
                if (
                    positional.preferred_mate is not None
                    and positional.preferred_mate
                    == (
                        self.x,
                        self.y,
                    )
                ):
                    self._birthChild(positional.genome)

    def onTimeIncremented(self):
        self._handleMovement()
        self._handleHealth()
        self._handleReproduction()
        if self.active_monomer == len(self.genome) - 1:
            self.active_monomer = 0
        else:
            self.active_monomer += 1
