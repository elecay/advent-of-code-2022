import os


__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

from typing import List, Callable


def read_file(path: str):
    with open(os.path.join(__location__, path)) as file:
        return file.read().splitlines()


def main(lines: List[str], engine: Callable):
    return engine(lines)
