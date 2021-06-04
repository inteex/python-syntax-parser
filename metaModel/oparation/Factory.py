from .Action import Action
from .ValueAction import ValueAction
from .SchemaAction import SchemaAction
from .RowAction import RowAction
from metaModel.Condition import Condition


def creatInstance(name: str, condition: Condition = None) -> Action:
    """Dynamically create Action sub-class if function is  supported
    by the metamodel, None otherwise

    Args:
        name (str): function name
        condition (Condition, optional): Defaults to None.

    Returns:
        Action: Action sub-class or None
    """
    schemaOperation = ["project", "dropna"]
    rowOperation = ["sort_values", "filter"]

    if rowOperation.__contains__(name):
        return RowAction(name + ": RowAction", condition)
    elif name == "apply":
        return ValueAction("format: ValueAction", condition)
    elif schemaOperation.__contains__(name):
        return SchemaAction(name + ": SchemaAction", condition)
    else:
        return None
