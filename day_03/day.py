import string
from typing import List

from utils import main, read_file

LINES = read_file("day_03/input.txt")

GROUP_SIZE = 3

alphabet = list(string.ascii_lowercase)
alphabet += [letter.upper() for letter in alphabet]
alphabet = [''] + alphabet


def engine_part_1(lines: List[str]):
    total_sum = 0
    for line in lines:
        compartment_size = int(len(line) / 2)
        first_compartment = set(line[:compartment_size])
        second_compartment = set(line[compartment_size:])
        common_item = first_compartment.intersection(second_compartment).pop()
        total_sum += alphabet.index(common_item)
    return total_sum


def engine_part_2(lines: List[str]):
    total_sum = 0
    common_items = set()
    for idx, line in enumerate(lines):
        if idx > 0 and idx % GROUP_SIZE == 0:
            common_item = common_items.pop()
            total_sum += alphabet.index(common_item)
            common_items = set(line)
        else:
            if len(common_items) == 0:
                common_items = set(line)
            else:
                common_items = common_items.intersection(set(line))
    common_item = common_items.pop()
    total_sum += alphabet.index(common_item)
    return total_sum


print(f"Part 1: {main(LINES, engine_part_1)}")
print(f"Part 2: {main(LINES, engine_part_2)}")
