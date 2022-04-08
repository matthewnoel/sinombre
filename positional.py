import random


class Positional:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y

    def onTimeIncremented(self):
        return

    def moveUp(self):
        if not self.world.isLocationAccessible(self.x, self.y + 1):
            return
        del self.world.position_relations[
            self.world.calculatePositionRelationIndex(self.x, self.y)
        ]
        self.world.position_relations[
            self.world.calculatePositionRelationIndex(self.x, self.y + 1)
        ] = self
        self.y += 1

    def moveRight(self):
        if not self.world.isLocationAccessible(self.x + 1, self.y):
            return
        del self.world.position_relations[
            self.world.calculatePositionRelationIndex(self.x, self.y)
        ]
        self.world.position_relations[
            self.world.calculatePositionRelationIndex(self.x + 1, self.y)
        ] = self
        self.x += 1

    def moveDown(self):
        if not self.world.isLocationAccessible(self.x, self.y - 1):
            return
        del self.world.position_relations[
            self.world.calculatePositionRelationIndex(self.x, self.y)
        ]
        self.world.position_relations[
            self.world.calculatePositionRelationIndex(self.x, self.y - 1)
        ] = self
        self.y -= 1

    def moveLeft(self):
        if not self.world.isLocationAccessible(self.x - 1, self.y):
            return
        del self.world.position_relations[
            self.world.calculatePositionRelationIndex(self.x, self.y)
        ]
        self.world.position_relations[
            self.world.calculatePositionRelationIndex(self.x - 1, self.y)
        ] = self
        self.x -= 1

    def moveRandom(self):
        rand = random.randrange(0, 4)
        if rand == 0:
            self.moveUp()
        elif rand == 1:
            self.moveRight()
        elif rand == 2:
            self.moveDown()
        elif rand == 3:
            self.moveLeft()
