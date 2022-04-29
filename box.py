class Box:
    def __init__(self):
        self.dict = {}
        self.legend = {"[q]": "Quit", "[space]": "Play/Pause"}

    def __repr__(self):
        retval = ""
        max = 0

        for key in self.dict:
            total = len(key) + len(str(self.dict[key]))
            if total > max:
                max = total
        for key in self.legend:
            total = len(key) + len(str(self.legend[key]))
            if total > max:
                max = total

        retval += self.getRowStr(max + 3)
        retval += "\n"
        retval += self.getDictStr(self.legend, max)
        retval += self.getDictStr(self.dict, max)
        retval += self.getRowStr(max + 3)

        return retval

    def set(self, key, value):
        self.dict[key] = value

    def getRowStr(self, size):
        retval = ""
        for i in range(0, size):
            retval += "-"
        return retval

    def getDictStr(self, dict, max):
        retval = ""
        for key in dict:
            retval += "|"
            retval += key
            for i in range(0, max + 1 - len(key) - len(str(dict[key]))):
                retval += " "
            retval += str(dict[key])
            retval += "|"
            retval += "\n"
        return retval
