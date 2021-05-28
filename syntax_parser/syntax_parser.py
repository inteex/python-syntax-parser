from transitions import Machine

from metaModel.Sequence import Sequence
from metaModel.oparation.Factory import creatInstance
from .utils.TokenHelper import isDot, isName, isRightParenthesis, isLeftParenthesis, isOpenBracket, isClosingBracket, isString


class Interpreter(object):
    """
    this is just a skeleton the class will be dynamically filled
    by Machine constructor (interface like)
    """

    def __init__(self):
        self.state = None


interpreter = Interpreter()

# The states
states = ['case_0', 'case_1', 'case_2', 'case_3', 'case_4', 'case_5', 'case_6',
          'case_7', 'case_8', 'case_9', 'case_10', 'case_11', 'case_12', 'case_13', 'case_14']

# trigger, current State => next State
transitions = []
# filling interpreter instance with state and transitions
machine = Machine(interpreter, states=states,
                  transitions=transitions, initial='case_0')

candidateFunctionName = ""
functions_stack = []
projectionParams = []
sequences: list[Sequence] = [Sequence()]


def handleAddOperationToSequence():
    if len(sequences[-1].operations):
        if sequences[-1].operations[-1].__class__.__name__ == "SchemaOperation"\
                and not functions_stack[-1].__class__.__name__ == "SchemaOperation":
            sequences.append(Sequence())
            sequences[-1].addOperation(functions_stack.pop())

        else:
            sequences[-1].addOperation(functions_stack.pop())
    else:
        sequences[-1].addOperation(functions_stack.pop())


def case_0(token):
    if isName(token):
        global candidateFunctionName
        candidateFunctionName = token.string
    elif isDot(token):
        machine.set_state('case_1')
    elif isLeftParenthesis(token):
        functions_stack.append(creatInstance(candidateFunctionName, "desc"))
        machine.set_state('case_2')
    elif isRightParenthesis(token):
        if functions_stack[-1] is None:
            functions_stack.pop()
        else:
            handleAddOperationToSequence()
    elif isOpenBracket(token):
        machine.set_state('case_3')


def case_1(token):
    machine.set_state('case_0')
    switcher.get(interpreter.state)(token)


def case_2(token):
    if isRightParenthesis(token):
        if functions_stack[-1] is None:
            functions_stack.pop()
        else:
            handleAddOperationToSequence()
    machine.set_state("case_0")


def case_3(token):
    if isOpenBracket(token):
        machine.set_state('case_4')
    elif isName(token):
        machine.set_state("case_6")


def case_4(token):
    if isClosingBracket(token):
        if len(projectionParams):
            functions_stack.append(creatInstance("project", projectionParams))
            handleAddOperationToSequence()
        machine.set_state("case_5")
    elif isString(token):
        projectionParams.append(token.string)


def case_5(token):
    if isClosingBracket(token):
        machine.set_state('case_1')
    else:
        print("error, case_5 can't have token: ", token.string)


def case_6(token):
    if isOpenBracket(token):
        machine.set_state('case_7')


def case_7(token):
    if isString(token):
        machine.set_state('case_8')

def case_8(token):
    if isClosingBracket(token):
        machine.set_state('case_9')

def case_9(token):
    if token == '==':
        machine.set_state('case10')

def case_10(token):
    machine.set_state('case_11')

def case_11(token):
    if isClosingBracket(token):
        machine.set_state('case_1')
    else:
        print("error")

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
    "case_3":  case_3,
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
            switcher.get(interpreter.state,
                         "this state does note exist")(token)
        except StopIteration:
            break
    # print(sequences)
    return sequences
