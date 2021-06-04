from functools import reduce

from transitions import Machine

from metaModel.Sequence import Sequence
from metaModel.oparation.Action import Action
from metaModel.oparation import Factory
from .utils import TokenHelper
from metaModel.Condition import Condition


class Interpreter(object):
    """
    this is just a skeleton the class will be dynamically filled
    by Machine constructor (interface like)
    """

    def __init__(self):
        self.state = None


interpreter = Interpreter()

# The states
states = [
    "case_0",
    "case_1",
    "case_2",
    "case_3",
    "case_4",
    "case_5",
    "case_6",
    "case_7",
    "case_8",
    "case_9",
    "case_10",
    "case_11",
    "case_12",
    "case_13",
    "case_14",
]

# trigger, current State => next State
transitions = []
# filling interpreter instance with state and transitions
machine = Machine(interpreter, states=states, transitions=transitions, initial="case_0")

candidateFunctionName = ""
functions_stack: list[Action] = []
functionParamsStack = []
projectionParams = []
sequences: list[Sequence] = [Sequence()]
filterColumn = ""
filterOp = ""
filterValue = ""


def handleAddOperationToSequence():
    params = functionParamsStack.pop()
    function = functions_stack.pop()
    function.condition = params
    if len(sequences[-1].operations):
        if (
            sequences[-1].operations[-1].__class__.__name__ == "SchemaOperation"
            and not function.__class__.__name__ == "SchemaOperation"
        ):
            sequences.append(Sequence())
            sequences[-1].addOperation(function)
        else:
            sequences[-1].addOperation(function)

    else:
        sequences[-1].addOperation(function)


def case_0(token):
    global functionParamsStack
    global candidateFunctionName
    if len(functions_stack):
        if not TokenHelper.isLeftParenthesis(token):
            functionParamsStack[-1] += str(token.string)
    if TokenHelper.isName(token):
        candidateFunctionName = token.string
    elif TokenHelper.isDot(token):
        machine.set_state("case_1")
    elif TokenHelper.isLeftParenthesis(token):
        action = Factory.creatInstance(candidateFunctionName)
        functions_stack.append(action)
        functionParamsStack.append(token.string)
    elif TokenHelper.isRightParenthesis(token):
        # ignore function that are note for data processing
        if functions_stack[-1] is None:
            functions_stack.pop()
            param = functionParamsStack.pop()
            if len(functionParamsStack):
                functionParamsStack[-1] += str(param)
        else:
            handleAddOperationToSequence()
    elif TokenHelper.isOpenBracket(token):
        machine.set_state("case_3")


def case_1(token):
    machine.set_state("case_0")
    switcher.get(interpreter.state)(token)


def case_2(token):
    pass


def case_3(token):

    if TokenHelper.isOpenBracket(token):
        machine.set_state("case_4")
    elif TokenHelper.isName(token):
        machine.set_state("case_6")
    elif TokenHelper.isString(token):
        machine.set_state("case_11")


def case_4(token):
    if TokenHelper.isClosingBracket(token):
        if len(projectionParams):
            txt = reduce(lambda acc, param: param + ", " + acc, projectionParams, "")
            print(txt)
            functions_stack.append(
                Factory.creatInstance("project", Condition(statement=str))
            )
            functionParamsStack.append(projectionParams)
            handleAddOperationToSequence()
        machine.set_state("case_5")
    elif TokenHelper.isString(token):
        projectionParams.append(token.string)


def case_5(token):
    if TokenHelper.isClosingBracket(token):
        machine.set_state("case_1")
    else:
        print("error, case_5 can't have token: ", token.string)


def case_6(token):
    if TokenHelper.isOpenBracket(token):
        machine.set_state("case_7")


def case_7(token):
    if TokenHelper.isString(token):
        global filterColumn
        filterColumn = token.string
        machine.set_state("case_8")


def case_8(token):
    if TokenHelper.isClosingBracket(token):
        machine.set_state("case_9")
    else:
        print("error case_8", token.string)


def case_9(token):
    if TokenHelper.isOperator(token):
        global filterOp
        filterOp = token.string
        machine.set_state("case_10")


def case_10(token):
    global filterValue, filterColumn, filterOp
    if TokenHelper.isClosingBracket(token):
        functions_stack.append(
            Factory.creatInstance(
                "filter", Condition(filterColumn, filterOp, filterValue)
            )
        )
        functionParamsStack.append(filterColumn + " " + filterOp + " " + filterValue)
        handleAddOperationToSequence()
        filterColumn = ""
        filterOp = ""
        filterValue = ""
        machine.set_state("case_1")
    else:
        filterValue += " " + str(token.string)


def case_11(token):
    if TokenHelper.isClosingBracket(token):
        machine.set_state("case_1")
    else:
        print("error case_11", token.string)


def case_12(token):
    pass


def case_13(token):
    pass


def case_14(token):
    pass


switcher = {
    "case_0": case_0,
    "case_1": case_1,
    "case_2": case_2,
    "case_3": case_3,
    "case_4": case_4,
    "case_5": case_5,
    "case_6": case_6,
    "case_7": case_7,
    "case_8": case_8,
    "case_9": case_9,
    "case_10": case_10,
    "case_11": case_11,
    "case_12": case_12,
    "case_13": case_13,
    "case_14": case_14,
}


def parse(tokens):
    while True:
        try:
            token = tokens.__next__()
            switcher.get(interpreter.state, "this state does note exist")(token)
        except StopIteration:
            break
    # print(sequences)
    return sequences
