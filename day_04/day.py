from typing import List

from utils import main, read_file

LINES = read_file("day_04/input.txt")


def engine_part_1(lines: List[str]):
    total_pairs = 0
    for line in lines:
        pair_one, pair_two = line.split(",")
        pair_one_min, pair_one_max = [int(n) for n in pair_one.split("-")]
        pair_two_min, pair_two_max = [int(n) for n in pair_two.split("-")]
        pair_one_in_pair_two = pair_one_min >= pair_two_min and pair_one_max <= pair_two_max
        pair_two_in_pair_one = pair_two_min >= pair_one_min and pair_two_max <= pair_one_max
        if pair_one_in_pair_two or pair_two_in_pair_one:
            total_pairs += 1
    return total_pairs


def engine_part_2(lines: List[str]):
    total_pairs = 0
    for line in lines:
        pair_one, pair_two = line.split(",")
        pair_one_min, pair_one_max = [int(n) for n in pair_one.split("-")]
        pair_two_min, pair_two_max = [int(n) for n in pair_two.split("-")]
        pair_one_min_overlap = pair_two_min <= pair_one_min <= pair_two_max
        pair_one_max_overlap = pair_two_min <= pair_one_max <= pair_two_max
        pair_two_min_overlap = pair_one_min <= pair_two_min <= pair_one_max
        pair_two_max_overlap = pair_one_min <= pair_two_max <= pair_one_max
        if pair_one_min_overlap or pair_one_max_overlap or pair_two_min_overlap or pair_two_max_overlap:
            total_pairs += 1
    return total_pairs


print(f"Part 1: {main(LINES, engine_part_1)}")
print(f"Part 2: {main(LINES, engine_part_2)}")
