from metaModel.Operation import Operation

default_file = "seq.txt"


def write(operations: list[Operation], path: str = default_file):
    f = open(path, "w")
    classesTxt = operation2pumlClass(operations)
    togetherText = together(operations)
    tuples2 = [(operations[i].name, operations[i + 1].name) for i in range(len(operations) - 1)]

    f.write("@startuml\n\n{}{}".format(classesTxt, togetherText))
    for tuple2 in tuples2:
        txt = "{} --> {}\n".format(tuple2[0], tuple2[1])
        f.write(txt)
    f.write("\n@enduml")


def together(operations: list[Operation]):
    txt = ""
    for operation in operations:
        txt += "    class {}\n".format(operation.name)
    return "together {\n" + str(txt) + "}\n\n"


def operation2pumlClass(operations: list[Operation]):
    txt = ""
    for operation in operations:
        txt += "class " + str(operation.name) + "{\n" + operation2properties(operation) + "}\n"
    return txt

def operation2properties(operation: Operation):
    txt = ""
    for p, value in vars(operation).items():
        txt += "    {} {}\n".format(p, value)
    return txt
