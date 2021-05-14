from transitions import Machine
from .utils.TokenHelper import isDot, isName, isRightParenthesis, isLeftParenthesis
from metaModel.Sequence import Sequence
from metaModel.oparation.Factory import creatInstance

class Interpreter(object):
    """
    this is just a skeleton the class will be dynamically filled
    by Machine constructor (interface like)
    """
    def __init__(self):
        self.state = None

    def dot(self):
        pass

    def leftParenthesis(self):
        pass

    def name(self):
        pass


interpreter = Interpreter()

# The states
states = ['name', 'nameDot', 'leftParenthesisState']  # ,  'rightParenthesisState']

# trigger, current State => next State
transitions = [
    ['name', 'nameDot', 'name'],
    ['name', 'leftParenthesisState', 'name'],
    ['dot', 'name', 'nameDot'],
    ['leftParenthesis', 'name', 'leftParenthesisState'],
]
# filling interpreter instance with state and transitions
machine = Machine(interpreter, states=states, transitions=transitions, initial='name')

candidateFunctionName = ""
functions_stack = []
sequences: list[Sequence] = [Sequence()]


def handleAddOperationToSequence():
    if len(sequences[-1].operations):
        if sequences[-1].operations[-1].__class__.__name__ == "SchemaOperation"\
                and not functions_stack[-1] == "SchemaOperation":
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


def nameDot(token):
    if isName(token):
        switcher.get("name")(token)
        interpreter.name()


def leftParenthesisState(token):
    if isRightParenthesis(token):
        handleAddOperationToSequence()
    # switch state to name
    interpreter.name()


switcher = {
    "name": name,
    "nameDot": nameDot,
    "leftParenthesisState": leftParenthesisState,
}


def parse_function_name(tokens):
    while True:
        try:
            token = tokens.__next__()
            switcher.get(interpreter.state, "this state does note exist")(token)
        except StopIteration:
            break
    print(sequences)
    return sequences


def parser(tokens):
    print(parse_function_name(tokens))
