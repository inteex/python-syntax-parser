import pandas as pd
from inspect import getmembers, isfunction
from functools import reduce
import operator


class FunctionsStack:
    functions: list = []

    @staticmethod
    def addFunction(name):
        FunctionsStack.functions.append(name)

    @staticmethod
    def filtredFunctions():
        pdFunctions: set = set([functionName[0] for functionName in getmembers(pd, isfunction)])
        dfFunctions: set = set([functionName[0] for functionName in getmembers(pd.DataFrame, isfunction)])
        concatenatedSet = reduce(operator.or_, [pdFunctions, dfFunctions])
        return [function for function in FunctionsStack.functions if function in concatenatedSet]

