class Box:
    def __init__(self):
        self.dict = {}

    def __repr__(self):
        retval = ""
        end_row = ""
        rows = ""
        max = 0

        for key in self.dict:
            total = len(key) + len(str(self.dict[key]))
            if total > max:
                max = total

        for key in self.dict:
            rows += "|"
            rows += key
            for i in range(0, max + 1 - len(key) - len(str(self.dict[key]))):
                rows += " "
            rows += str(self.dict[key])
            rows += "|"
            rows += "\n"

        for i in range(0, max + 3):
            end_row += "-"

        retval += end_row
        retval += "\n"
        retval += rows
        retval += end_row

        return retval

    def set(self, key, value):
        self.dict[key] = value
