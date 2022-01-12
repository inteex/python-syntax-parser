from metaModel.Sequence import Sequence
from metaModel.oparation.Action import Action
from metaModel.oparation import Factory
from metaModel.Condition import Condition
from syntax_parser.StateMachine import StateMachine
from .utils import TokenHelper

# The states
states = [
    "case_0",
    "case_1",
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

# filling interpreter instance with state and transitions
machine = StateMachine(states=states, initial="case_0")

candidateFunctionName = ""
functions_stack: list[Action] = []
functionParamsStack = []
projectionParams = []
sequences: list[Sequence] = [Sequence()]
filterColumn = ""
filterOp = ""
filterValue = ""


def handleAddOperationToSequence(isNewSeq=False):
    if isNewSeq is not True:
        params = functionParamsStack.pop()
        function = functions_stack.pop()
        function.condition = params
        sequences[-1].addOperation(function)
    else:
        sequences.append(Sequence())


def case_0(token):
    global functionParamsStack  # pylint: disable=global-statement
    global candidateFunctionName  # pylint: disable=global-statement
    if len(functions_stack) > 0:
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
            if len(functionParamsStack) > 0:
                functionParamsStack[-1] += str(param)
        else:
            handleAddOperationToSequence()
    elif TokenHelper.isOpenBracket(token):
        machine.set_state("case_3")
    elif TokenHelper.isNewSequence(token):
        handleAddOperationToSequence(True)


def case_1(token):
    machine.set_state("case_0")
    switcher.get(machine.currentState)(token)


def case_3(token):

    if TokenHelper.isOpenBracket(token):
        machine.set_state("case_4")
    elif TokenHelper.isName(token):
        machine.set_state("case_6")
    elif TokenHelper.isString(token):
        machine.set_state("case_11")


def case_4(token):
    if TokenHelper.isClosingBracket(token):
        if len(projectionParams) > 0:
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
        global filterColumn  # pylint: disable=global-statement
        filterColumn = token.string
        machine.set_state("case_8")


def case_8(token):
    if TokenHelper.isClosingBracket(token):
        machine.set_state("case_9")
    else:
        print("error case_8", token.string)


def case_9(token):
    if TokenHelper.isOperator(token):
        global filterOp  # pylint: disable=global-statement
        filterOp = token.string
        machine.set_state("case_10")


def case_10(token):
    global filterValue, filterColumn, filterOp  # pylint: disable=global-statement
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


switcher = {
    "case_0": case_0,
    "case_1": case_1,
    "case_3": case_3,
    "case_4": case_4,
    "case_5": case_5,
    "case_6": case_6,
    "case_7": case_7,
    "case_8": case_8,
    "case_9": case_9,
    "case_10": case_10,
    "case_11": case_11,
}


def parse(tokens):
    while True:
        try:
            token = tokens.__next__()
            switcher.get(machine.currentState, "this state does note exist")(token)
        except StopIteration:
            break
    # print(sequences)
    return sequences
