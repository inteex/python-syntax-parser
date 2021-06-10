from metaModel.oparation.Action import Action
from metaModel.Sequence import Sequence
import config

default_path = "/".join([config.build_directory, config.file_name])


def write(sequences: "list[Sequence]", path: str = default_path):
    f = open(path, "w")
    f.write('@startuml\
        \nskinparam classFontColor automatic\
        \nskinparam classHeaderBackgroundColor #9DCCB8\
        \nskinparam classBackgroundColor #fff\
        \nskinparam classBorderColor #99C49B\
        \nskinparam packageBorderColor #353fb0\
        \n\n\
        \nclass "csvFile" #e3cb84{\
            \n{field} filename "meteo.csv"\
            \n{field} provider null\
        \n}\n\n')
    for i, sequence in enumerate(sequences):
        classesTxt = operation2pumlClass(sequence.operations)
        togetherText = together(sequence.operations)
        tuples2 = [
            (sequence.operations[i].name, sequence.operations[i + 1].name)
            for i in range(len(sequence.operations) - 1)
        ]

        f.write('package "sequence ' + str(i + 1) + '" {\n')
        f.write("{}{}".format(classesTxt, togetherText))
        for tuple2 in tuples2:
            txt = '"{}" --> "{}"\n'.format(tuple2[0], tuple2[1])
            f.write(txt)
        f.write("\n}\n")
        f.write('"csvFile" --> "sequence ' + str(i + 1) + '"\n')
    f.write("\n@enduml")


def together(operations: "list[Action]"):
    txt = ""
    for operation in operations:
        txt += '    class "{}"\n'.format(operation.name)
    return "together {\n" + str(txt) + "}\n\n"


def operation2pumlClass(operations: "list[Action]"):
    txt = ""
    for operation in operations:
        txt += (
            'class "'
            + str(operation.name)
            + '"{\n'
            + operation2properties(operation)
            + "}\n"
        )
    return txt


def operation2properties(operation: Action):
    txt = ""
    for p, value in vars(operation).items():
        if not p == "name":
            txt += "    {field} " + "{} {}\n".format(p, value)
    return txt


def package(operations: "list[Action]"):
    txt = ""
    for operation in operations:
        txt += '    class "{}"\n'.format(operation.name)
    return "package {\n" + str(txt) + "}\n\n"
