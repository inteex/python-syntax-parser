import tokenize
from syntax_parser import parser

with tokenize.open('./samples/sample2.py') as f:
    print("Start parsing ...")
    tokens = tokenize.generate_tokens(f.readline)
    parser(tokens)
