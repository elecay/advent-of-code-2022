import math
from collections import defaultdict
from typing import Dict, List

from utils import main, read_file

LINES = read_file("day_05/input.txt")


def engine_part_1(lines: List[str]):
    stack_lines = []
    stacks = []
    getting_stack_lines = True
    for line in lines:
        if not line:
            continue
        elif line[1] == "1":
            stacks = _build_stacks(stack_lines)
            getting_stack_lines = False
            continue

        if getting_stack_lines:
            stack_lines.append(line)
        else:
            _apply_move_to_stacks(stacks, line)

    return _get_top_crates(stacks)


def engine_part_2(lines: List[str]):
    pass


def _build_stacks(lines: List[str]) -> Dict[int, List[str]]:
    stacks = defaultdict(list)
    crates = math.ceil(len(lines[0]) / 4)
    idx = 0
    for line in lines:
        for i in range(0, len(line), 4):
            crate = line[i : i + 4].strip().replace("[", "").replace("]", "")
            if crate:
                stacks[idx % crates] = [crate] + stacks[idx % crates]
            idx += 1
    return stacks


def _apply_move_to_stacks(stacks: Dict[int, List[str]], move: str):
    _, amount_to_move, _, from_stack, _, to_stack = move.split(" ")
    amount_to_move = int(amount_to_move)
    from_stack = int(from_stack) - 1
    to_stack = int(to_stack) - 1

    crates_moved = stacks[from_stack][-amount_to_move:]
    crates_moved.reverse()
    stacks[from_stack] = stacks[from_stack][: len(stacks[from_stack]) - amount_to_move]
    stacks[to_stack] += crates_moved


def _get_top_crates(stacks: Dict[int, List[str]]) -> str:
    top_cranes = ""
    for idx in range(len(stacks)):
        top_cranes += stacks[idx][-1:][0]
    return top_cranes


print(f"Part 1: {main(LINES, engine_part_1)}")
print(f"Part 2: {main(LINES, engine_part_2)}")
