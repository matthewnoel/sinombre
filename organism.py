import random

from monomer import Monomer
from positional import Positional


def getRandomGenome():
    return [Monomer(10)]


class Organism(Positional):
    def __init__(self, world, x, y, genome=None):
        if genome is None:
            genome = getRandomGenome()
        self.genome = genome
        self.health = 30
        self.initial_health = 30
        self.preferred_mate = None
        Positional.__init__(self, world, x, y)

    def __repr__(self):
        value = self.genome[0].value
        bg = 40 + int(value * 7 / 10)
        fg = 30
        if bg == 40 or bg == 44:
            fg = 37
        return "\033[0;" + str(fg) + ";" + str(bg) + "m" + "X" + "\033[0;0m"

    def _handleMovement(self):
        value = self.genome[0].value
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

    def _handleHealth(self):
        self.health -= 1
        self.health += self.world.calculateOasisBoost(self.x, self.y)
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
                        int(
                            (1 - self.health / self.initial_health)
                            * self.health
                        ),
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
                if random.randrange(0, 500) == 0:
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
