import random


class Monomer:
    def __init__(self, range, value=None):
        if value is None:
            value = random.randrange(0, range)
        self.range = range
        self.value = value

    def mutate(self):
        if self.value == self.range - 1:
            self.value = 0
        else:
            self.value += 1
