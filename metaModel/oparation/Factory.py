import yaml
from metaModel.Condition import Condition
from .Action import Action
from .ValueAction import ValueAction
from .SchemaAction import SchemaAction
from .RowAction import RowAction


def creatInstance(name: str, condition: Condition = None) -> Action or None:
    """Dynamically create Action sub-class if function is  supported
    by the metamodel, None otherwise

    Args:
        name (str): function name
        condition (Condition, optional): Defaults to None.

    Returns:
        Action: Action sub-class or None
    """
    schemaAction, rowAction, valueAction = {}, {}, {}

    with open("actions.yaml", encoding="utf-8") as actionsFile:
        actions = yaml.load(actionsFile, Loader=yaml.FullLoader)
        schemaAction = actions["schemaAction"]
        rowAction = actions["rowAction"]
        valueAction = actions["valueAction"]

    if rowAction.__contains__(name):
        return RowAction(name, condition, rowAction[name])
    if valueAction.__contains__(name):
        return ValueAction(name, condition, valueAction[name])
    if schemaAction.__contains__(name):
        return SchemaAction(name, condition, schemaAction[name])
    return None
