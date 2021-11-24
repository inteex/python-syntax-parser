from metaModel.Condition import Condition
from .Action import Action
from .ValueAction import ValueAction
from .SchemaAction import SchemaAction
from .RowAction import RowAction


def creatInstance(
    name: str, condition: Condition = None, description: str = '""'
) -> Action or None:
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
        return RowAction(name, condition, description)
    if name == "apply":
        return ValueAction("format", condition, description)
    if schemaOperation.__contains__(name):
        if name == "dropna":
            description = '"drop NaN values following\n desired axis"'
        return SchemaAction(name, condition, description)
    return None
