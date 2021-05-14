class Operation:
    order: int

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return "{} - {} ({})".format(self.name, self.description, self.order)

    def __repr__(self):
        return self.__str__()
