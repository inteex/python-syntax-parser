from .ValueOperation import ValueOperation
from .SchemaOperation import SchemaOperation
from .RowOperation import RowOperation


def creatInstance(name: str, desc: str):
    if name == "sort_values":
        return RowOperation(name, desc)
    elif name == "apply":
        return ValueOperation(name, desc)
    elif name == "dropna":
        return SchemaOperation(name, desc)
    else:
        return None
