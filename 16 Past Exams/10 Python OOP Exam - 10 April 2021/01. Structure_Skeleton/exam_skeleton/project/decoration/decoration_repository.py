class DecorationRepository:
    def __init__(self):
        self.decorations = []

    def add(self, decoration):
        self.decorations.append(decoration)

    def remove(self, decoration):
        if decoration not in self.decorations:
            return False

        self.decorations.remove(decoration)

        return True

    def find_by_type(self, decoration_type: str):
        for decoration in self.decorations:
            if decoration.decoration_type == decoration_type:
                return decoration

        return "None"

