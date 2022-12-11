import os
from typing import Callable, List


def read_file(path: str):
    base_path = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(base_path, path)) as file:
        return file.read().splitlines()


def main(lines: List[str], engine: Callable):
    return engine(lines)
