from transitions import Machine
from .functionsStack import FunctionsStack
from .utils.TokenHelper import isDot, isName, isRightParenthesis, isLeftParenthesis


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


def name(token):
    if isName(token):
        global candidateFunctionName
        candidateFunctionName = token.string

    if isDot(token):
        interpreter.dot()
    elif isLeftParenthesis(token):
        functions_stack.append(candidateFunctionName)
        interpreter.leftParenthesis()
    elif isRightParenthesis(token):
        FunctionsStack.addFunction(functions_stack.pop())


def nameDot(token):
    if isName(token):
        switcher.get("name")(token)
        interpreter.name()


def leftParenthesisState(token):
    if isRightParenthesis(token):
        FunctionsStack.addFunction(functions_stack.pop())
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
    return FunctionsStack.functions


def parser(tokens):
    print((parse_function_name(tokens)))