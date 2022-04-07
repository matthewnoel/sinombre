class Organism:
    def _getRandomGenome():
        return "A"

    def __init__(self, location, genome=_getRandomGenome()):
        self.location = location
        self.genome = genome

    def __repr__(self):
        return self.genome

    def incrementTime(self):
        return
