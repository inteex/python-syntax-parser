default_file = "seq.txt"


def write(functions: list, path: str = default_file):
    f = open(path, "w")
    togetherText = together(functions)
    tuples2 = [((functions[i]), functions[i + 1]) for i in range(len(functions) - 1)]

    f.write("@startuml\n\n{}".format(togetherText))
    for tuple2 in tuples2:
        txt = "{} --> {}\n".format(tuple2[0], tuple2[1])
        f.write(txt)
    f.write("\n@enduml")


def together(functions):
    txt = ""
    for function in functions:
        txt += "    class {}\n".format(function)
    return "together {\n"+str(txt)+"}\n\n"
