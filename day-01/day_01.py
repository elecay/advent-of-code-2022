from typing import List

from utils import read_file

lines_example = read_file("day-01/example.txt")
lines_input = read_file("day-01/input.txt")


def main(part: int, run_input: bool = False):
    lines = lines_example
    if run_input:
        lines = lines_input

    if part == 1:
        return engine_part_1(lines)
    return engine_part_2(lines)


def engine_part_1(lines: List[str]):
    elf_cal = get_elf_cal(lines)
    _, elf_cals = elf_cal[0]
    return elf_cals


def engine_part_2(lines: List[str]):
    elf_cal = get_elf_cal(lines)
    elf_cals_sum = 0
    for i in range(3):
        _, elf_cals = elf_cal[i]
        elf_cals_sum += elf_cals
    return elf_cals_sum


def get_elf_cal(lines: List[str]):
    elf_cal = {}
    idx = 1
    current_sum = 0

    for line in lines:
        if not line:
            elf_cal[idx] = current_sum
            idx += 1
            current_sum = 0
            continue
        current_sum += int(line)

    elf_cal[idx + 1] = current_sum
    return sorted(elf_cal.items(), key=lambda item: -item[1])


print(f"Part 1: {main(1, True)}")
print(f"Part 2: {main(2, True)}")
