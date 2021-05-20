from .ValueOperation import ValueOperation
from .SchemaOperation import SchemaOperation
from .RowOperation import RowOperation


def creatInstance(name: str, params: str):
    schemaOperation = ["project", "dropna"]
    if name == "sort_values":
        return RowOperation("sort: RowOperation", params)
    elif name == "apply":
        return ValueOperation("format: ValueOperation", params)
    elif schemaOperation.__contains__(name):
        return SchemaOperation(name + ": SchemaOperation", params)
    else:
        return None
