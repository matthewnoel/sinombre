from positional import Positional


class Oasis(Positional):
    def __init__(self, world, x, y):
        self.emittance = 0.7
        Positional.__init__(self, world, x, y)

    def __repr__(self):
        return "\033[0;32;47m" + "+" + "\033[0;0m"
