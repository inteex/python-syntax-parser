[![Version](https://img.shields.io/badge/version-v0.1-orange.svg)](https://github.com/inteex/python-syntax-parser)

A prototype Python syntax parser for the interpretation of the processing on data. 

## Installation

installing pipenv

    pip install pipenv

for help on windows you can follow this [link](https://www.pythontutorial.net/python-basics/install-pipenv-windows/).

## Table of Contents
- [Quickstart](#quickstart)
- [Know issues](#know-issues)
- [Non-Quickstart](#the-non-quickstart)
    - [Basic initialization](#basic-initialization)
- [Bug](#Bug)

## Quickstart
    pipenv shell
    (python virtualenv): pipenv install

### Filling envirennement variables

- create `.env` file on the root of the project .
- copy `.env.example` to `.env`.
- replace values.

Example `.env` file:
```
BUILD_DIRECTORY="build"
FILE_NAME="puml.txt"
PYTHON_FILE_SAMPLE= "./samples/sample2.py"
```

### Good to go!
inside your virtual env run:

    python main.py

check you build folder ;) !
   
## Know issues

If you are using vscode and getting unresolved module warnings you should add somthing like this to .vscode/setting.json

linux:
```json
{
    "python.analysis.extraPaths": [
        "/home/YOUR_USER_NAME/.local/share/virtualenvs/python-syntax-parser-XXXXXXXX/lib/python3.9/site-packages"
    ]
}
```

Windows:
```json
{
    "python.analysis.extraPaths": [
        "C:/Users/YOUR_USER_NAME/.virtualenvs/python-syntax-parser-XXXXXXXX/Lib/site-packages"
    ]
}

```

## The non-quickstart

### Basic initialization
    # TODO 

## Bug ?

Reports and other issues, please open an issue on GitHub.

For any other questions, solicitations, or large unrestricted monetary gifts, email [Reda mekhezzem](mailto:reda.mekhezzem@ensma.fr).
