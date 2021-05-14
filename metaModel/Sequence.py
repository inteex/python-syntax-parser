import uuid
from metaModel.oparation.Operation import Operation


class Sequence:

    def __init__(self):
        self.sequenceId = uuid.uuid4()
        self.operations = []
        self.order = 0

    def addOperation(self, operation: Operation):
        self.order += 1
        operation.order = self.order
        self.operations.append(operation)

    def __str__(self):
        return self.operations.__str__()

    def __repr__(self):
        return self.__str__()