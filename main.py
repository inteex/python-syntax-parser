import tokenize
from syntax_parser import parse
from puml.PumlWriter import write
import subprocess
from loaders import SpinningLoader
from pathlib import Path

BUILD_DIRECTORY = "build"
Path(BUILD_DIRECTORY).mkdir(parents=True, exist_ok=True)

loader = SpinningLoader()
with tokenize.open('./samples/sample2.py') as f:
    tokens = tokenize.generate_tokens(f.readline)
    sequences = parse(tokens)
    write(sequences, path="{}/seq.txt".format(BUILD_DIRECTORY))
    loader.text = "generating class diagram ..."
    loader.start()
    # show loader because it takes some time
    subprocess.call(['java', '-jar', 'lib/plantuml.jar', '{}/seq.txt'.format(BUILD_DIRECTORY)])
    loader.complete_text = "Class diagram generated with success!"
    loader.stop()
    print("PNG file created!")