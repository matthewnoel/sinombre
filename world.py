import random

from block import Block


class World:
    def __init__(self, size):
        blocks = []
        for x in range(size):
            row = []
            for y in range(size):
                block = Block(x, y)
                if random.randrange(1, 11) % 10 == 0:
                    block.spawnOrganism()
                row.append(block)
            blocks.append(row)
        self.blocks = blocks

    def __repr__(self):
        retval = ""
        for i in self.blocks:
            for j in i:
                retval += str(j)
            retval += "\n"
        return retval

    def incrementTime(self):
        for i in self.blocks:
            for j in i:
                j.incrementTime()
