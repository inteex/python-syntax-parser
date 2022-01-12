from token import COMMENT, NAME, OP, STRING
from tokenize import TokenInfo


SEQUENCE_DECORATOR = "@newSeq"


def isName(token: TokenInfo):
    return token.type == NAME


def isDot(token: TokenInfo):
    return token.type == OP and token.string == "."


def isLeftParenthesis(token: TokenInfo):
    return OP == token.type and token.string == "("


def isRightParenthesis(token: TokenInfo):
    return OP == token.type and token.string == ")"


def isOpenBracket(token: TokenInfo):
    return OP == token.type and token.string == "["


def isClosingBracket(token: TokenInfo):
    return OP == token.type and token.string == "]"


def isString(token: TokenInfo):
    return STRING == token.type


def isOperator(token: TokenInfo):
    return OP == token.type


def isNewSequence(token: TokenInfo):
    return COMMENT == token.type and isNewSeqComment(token.string)


def isNewSeqComment(comment: str):
    return comment.replace("#", "").strip().startswith(SEQUENCE_DECORATOR)
