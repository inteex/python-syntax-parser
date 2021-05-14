import uuid
from metaModel.Operation import Operation


class Sequence:
    operations = []
    order = 0

    def __init__(self):
        self.sequenceId = uuid.uuid4()

    def addOperation(self, operation: Operation):
        self.order += 1
        operation.order = self.order
        self.operations.append(operation)

    def __str__(self):
        return self.operations.__str__()
