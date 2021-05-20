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
states = ['name', 'nameDot', 'leftParenthesisState', 'nameOpenBracket', 'nameOBOB']  # ,  'rightParenthesisState']

# trigger, current State => next State
transitions = [
    ['name', 'nameDot', 'name'],
    ['name', 'leftParenthesisState', 'name'],
    ['dot', 'name', 'nameDot'],
    ['leftParenthesis', 'name', 'leftParenthesisState'],
    ['openBracket', 'name', 'nameOpenBracket'],
    ['openBracket', 'nameOpenBracket', 'nameOBOB'],
]
# filling interpreter instance with state and transitions
machine = Machine(interpreter, states=states, transitions=transitions, initial='name')

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


def name(token):
    if isName(token):
        global candidateFunctionName
        candidateFunctionName = token.string

    if isDot(token):
        interpreter.dot()
    elif isLeftParenthesis(token):
        functions_stack.append(creatInstance(candidateFunctionName, "desc"))
        interpreter.leftParenthesis()
    elif isRightParenthesis(token):
        if functions_stack[-1] is None:
            functions_stack.pop()
        else:
            handleAddOperationToSequence()
    elif isOpenBracket(token):
        interpreter.openBracket()


def nameDot(token):
    if isName(token):
        switcher.get("name")(token)
        interpreter.name()


def leftParenthesisState(token):
    if isRightParenthesis(token):
        if functions_stack[-1] is None:
            functions_stack.pop()
        else:
            handleAddOperationToSequence()
    # switch state to name
    machine.set_state("name")


def nameOpenBracket(token):
    if isOpenBracket(token):
        interpreter.openBracket()
    else:
        machine.set_state("name")


def nameOBOB(token):
    if isClosingBracket(token):
        if len(projectionParams):
            functions_stack.append(creatInstance("project", projectionParams))
            handleAddOperationToSequence()
        machine.set_state("name")
    elif isString(token):
        projectionParams.append(token.string)


switcher = {
    "name": name,
    "nameDot": nameDot,
    "leftParenthesisState": leftParenthesisState,
    "nameOpenBracket":  nameOpenBracket,
    "nameOBOB": nameOBOB
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
