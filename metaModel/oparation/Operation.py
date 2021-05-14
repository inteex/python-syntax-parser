class Operation(object):
    order: int

    def __init__(self, name, description):
        self.order = 1
        self.name = name
        self.description = description

    # to loop over all operation element and call str function
    def __repr__(self):
        return "{}: {} - {} ({})".format(type(self).__name__, self.name, self.description, self.order)
