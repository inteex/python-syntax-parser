import pandas as pd
class FunctionsStack:
    functions: list = []

    @staticmethod
    def addFunction(name):
        FunctionsStack.functions.append(name)

    @staticmethod
    def pandaFunctions():
        pd.f