import random


class Positional:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y

    @staticmethod
    def transformations():
        return [
            (0, 1),
            (1, 1),
            (1, 0),
            (-1, 1),
            (-1, 0),
            (-1, -1),
            (-1, 0),
            (-1, 1),
        ]

    def onTimeIncremented(self):
        return

    def move(self, x, y):
        if not self.world.isLocationAccessible(self.x + x, self.y + y):
            return
        del self.world.position_relations[
            self.world.calculatePositionRelationIndex(self.x, self.y)
        ]
        self.world.position_relations[
            self.world.calculatePositionRelationIndex(self.x + x, self.y + y)
        ] = self
        self.x += x
        self.y += y

    def moveNorth(self):
        self.move(0, 1)

    def moveNorthEast(self):
        self.move(1, 1)

    def moveEast(self):
        self.move(1, 0)

    def moveSouthEast(self):
        self.move(1, -1)

    def moveSouth(self):
        self.move(0, -1)

    def moveSouthWest(self):
        self.move(-1, -1)

    def moveWest(self):
        self.move(-1, 0)

    def moveNorthWest(self):
        self.move(-1, 1)

    def moveRandom(self):
        rand = random.randrange(0, 8)
        if rand == 0:
            self.moveNorth()
        elif rand == 1:
            self.moveNorthEast()
        elif rand == 2:
            self.moveEast()
        elif rand == 3:
            self.moveSouthEast()
        elif rand == 4:
            self.moveSouth()
        elif rand == 5:
            self.moveSouthWest()
        elif rand == 6:
            self.moveWest()
        elif rand == 7:
            self.moveNorthWest()

    def remove(self):
        del self.world.position_relations[
            self.world.calculatePositionRelationIndex(self.x, self.y)
        ]
