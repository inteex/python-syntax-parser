import enum


class TokenTypes(enum.Enum):
    OP = 54
    NAME = 1
    NEWLINE = 4
    NL = 61
    STRING = 3


def isName(token):
    return token.type == TokenTypes.NAME.value


def isDot(token):
    return token.type == TokenTypes.OP.value and token.string == "."


def isLeftParenthesis(token):
    return TokenTypes.OP.value == token.type and token.string == '('


def isRightParenthesis(token):
    return TokenTypes.OP.value == token.type and token.string == ')'


def isOpenBracket(token):
    return TokenTypes.OP.value == token.type and token.string == '['


def isClosingBracket(token):
    return TokenTypes.OP.value == token.type and token.string == ']'


def isString(token):
    return TokenTypes.STRING.value == token.type


def isOperator(token):
    return TokenTypes.OP.value == token.type
