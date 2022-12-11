from typing import List

from utils import main, read_file

LINES = read_file("day_01/input.txt")


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


print(f"Part 1: {main(LINES, engine_part_1)}")
print(f"Part 2: {main(LINES, engine_part_2)}")
