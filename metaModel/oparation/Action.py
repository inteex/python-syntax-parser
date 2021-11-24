from metaModel.Condition import Condition


class Action:
    order: int

    def __init__(self, name, condition: Condition, description: str):
        self.order = 1
        # example 'filter: RowAction'
        self.name = name + ": " + self.__class__.__name__
        self.condition = condition
        self.description = description

    # to loop over all operation element and call str function
    def __repr__(self):
        return "{}: {} - {} ({})".format(
            type(self).__name__, self.name, self.condition, self.order
        )
