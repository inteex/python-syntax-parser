from metaModel.oparation.Operation import Operation
from metaModel.Sequence import Sequence

default_file = "seq.txt"


def write(sequences: list[Sequence], path: str = default_file):
    f = open(path, "w")
    f.write("@startuml\n\n")
    for i, sequence in enumerate(sequences):
        classesTxt = operation2pumlClass(sequence.operations)
        togetherText = together(sequence.operations)
        tuples2 = [(sequence.operations[i].name, sequence.operations[i + 1].name) for i in
                   range(len(sequence.operations) - 1)]

        f.write("package \"sequence " + str(i + 1)+"\" {\n")
        f.write("{}{}".format(classesTxt, togetherText))
        for tuple2 in tuples2:
            txt = "\"{}\" --> \"{}\"\n".format(tuple2[0], tuple2[1])
            f.write(txt)
        f.write("\n}\n")
    f.write("\n@enduml")


def together(operations: list[Operation]):
    txt = ""
    for operation in operations:
        txt += "    class \"{}\"\n".format(operation.name)
    return "together {\n" + str(txt) + "}\n\n"


def operation2pumlClass(operations: list[Operation]):
    txt = ""
    for operation in operations:
        txt += "class \"" + str(operation.name) + "\"{\n" + operation2properties(operation) + "}\n"
    return txt


def operation2properties(operation: Operation):
    txt = ""
    for p, value in vars(operation).items():
        if not p == "name":
            txt += "    {field} " + "{} {}\n".format(p, value)
    return txt


def package(operations: list[Operation]):
    txt = ""
    for operation in operations:
        txt += "    class \"{}\"\n".format(operation.name)
    return "package {\n" + str(txt) + "}\n\n"
