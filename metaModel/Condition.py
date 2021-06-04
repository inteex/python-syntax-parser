class Condition:
    def __init__(self, statement="", operator="", value=""):
        self.statement = statement
        self.operator = operator
        self.value = value

    def __str__(self):
        return "{} {} {}".format(self.statement, self.operator, self.value)
