class Operation(object):
    order: int

    def __init__(self, name, params):
        self.order = 1
        self.name = name
        self.params = params

    # to loop over all operation element and call str function
    def __repr__(self):
        return "{}: {} - {} ({})".format(type(self).__name__, self.name, self.params, self.order)
