import tokenize
from syntax_parser import parse
from puml.PumlWriter import write
import subprocess
from loaders import SpinningLoader
from pathlib import Path
import config

BUILD_DIRECTORY = config.build_directory
FILE_NAME = config.file_name
Path(BUILD_DIRECTORY).mkdir(parents=True, exist_ok=True)
path = "/".join([config.build_directory, config.file_name])

loader = SpinningLoader()
with tokenize.open(config.python_file_sample) as f:
    tokens = tokenize.generate_tokens(f.readline)
    sequences = parse(tokens)
    write(sequences, path)
    loader.text = "generating class diagram ..."
    loader.start()
    # show loader because it takes some time
    subprocess.call(["java", "-jar", "lib/plantuml.jar", path])
    loader.complete_text = "Class diagram generated with success!"
    loader.stop()
    print("PNG file created! at {}".format(path))
