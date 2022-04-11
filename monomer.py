import random


class Monomer:
    def __init__(self, range, value=None):
        if value is None:
            value = random.randrange(0, range)
        self.range = range
        self.value = value

    def mutate(self):
        new_value = random.randrange(0, self.range)
        while self.value == new_value:
            new_value = random.randrange(0, self.range)
        self.value = new_value
