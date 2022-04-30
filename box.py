class Box:
    def __init__(self):
        self.dict = {}
        self.controls = {"q": "Quit", "space": "Play/Pause", "n": "Next step"}

    def __repr__(self):
        retval = ""
        max = 0
        retval += "\n"
        retval += self.getDictStr(self.dict, lambda key: "|" + key)
        retval += self.getDictStr(self.controls, lambda key: "[" + key + "]")

        return retval

    def set(self, key, value):
        self.dict[key] = value

    def getRowStr(self, size):
        retval = ""
        for i in range(0, size):
            retval += "-"
        retval += "\n"
        return retval

    def getMaxEntryLength(self, dict):
        max = 0
        for key in dict:
            total = len(key) + len(str(dict[key]))
            if total > max:
                max = total
        return max

    def getDictStr(self, dict, key_transform):
        max = self.getMaxEntryLength(dict)
        retval = ""
        rows = ""
        transform_offset = 0
        for key in dict:
            transformed_key = key_transform(key)
            transform_offset = len(transformed_key) - len(key)
            rows += transformed_key
            for i in range(0, max + 1 - len(key) - len(str(dict[key]))):
                rows += " "
            rows += str(dict[key])
            rows += "|"
            rows += "\n"
        retval += self.getRowStr(max + 2 + transform_offset)
        retval += rows
        retval += self.getRowStr(max + 2 + transform_offset)
        return retval
