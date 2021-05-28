from .ValueOperation import ValueOperation
from .SchemaOperation import SchemaOperation
from .RowOperation import RowOperation


def creatInstance(name: str, params: str):
    schemaOperation = ["project", "dropna"]
    rowOperation = ["sort_values", "filter"]
    if rowOperation.__contains__(name):
        return RowOperation(name + ": RowOperation", params)
    elif name == "apply":
        return ValueOperation("format: ValueOperation", params)
    elif schemaOperation.__contains__(name):
        return SchemaOperation(name + ": SchemaOperation", params)
    else:
        return None
