import tokenize
from syntax_parser import parse
from puml.PumlWriter import write
import subprocess
from loaders import SpinningLoader, BarLoader
from pathlib import Path
import config
from loading import withLoader

BUILD_DIRECTORY = config.build_directory
FILE_NAME = config.file_name
Path(BUILD_DIRECTORY).mkdir(parents=True, exist_ok=True)
path = "/".join([config.build_directory, config.file_name])


with tokenize.open(config.python_file_sample) as f:
    tokens = tokenize.generate_tokens(f.readline)
    sequences = withLoader("parsing tokens ...", SpinningLoader(), parse, tokens)
    write(sequences, path)
    # show loader because it takes some time
    withLoader(
        "generating class diagram ...",
        SpinningLoader(),
        subprocess.call,
        ["java", "-jar", "lib/plantuml.jar", path],
    )
    print("PNG file created! at {}".format(path))
