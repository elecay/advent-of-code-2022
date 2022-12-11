from typing import List

from utils import main, read_file

LINES = read_file("day_02/input.txt")

SHAPE_PTS_MAPPER = {"A": 1, "B": 2, "C": 3}

SHAPES_EQUIVALENCE = {"X": "A", "Y": "B", "Z": "C"}

WINNER_MAPPER = {"A": "B", "B": "C", "C": "A"}

GAME_PTS_RESULT = {"WIN": 6, "DRAW": 3, "LOST": 0}

SHAPES_RESULT_MAPPER = {
    "A": {"Z": WINNER_MAPPER["A"], "X": "C", "Y": "A"},
    "B": {"Z": WINNER_MAPPER["B"], "X": "A", "Y": "B"},
    "C": {"Z": WINNER_MAPPER["C"], "X": "B", "Y": "C"},
}


def engine_part_1(lines: List[str]):
    total_points = 0
    for line in lines:
        opponent_shape, my_shape = line.split(" ")
        my_shape = SHAPES_EQUIVALENCE[my_shape]

        total_points += SHAPE_PTS_MAPPER[my_shape]
        if WINNER_MAPPER[opponent_shape] == my_shape:
            total_points += GAME_PTS_RESULT["WIN"]
        elif opponent_shape == my_shape:
            total_points += GAME_PTS_RESULT["DRAW"]

    return total_points


def engine_part_2(lines: List[str]):
    total_points = 0
    for line in lines:
        opponent_shape, game_result = line.split(" ")
        my_shape = SHAPES_RESULT_MAPPER[opponent_shape][game_result]

        total_points += SHAPE_PTS_MAPPER[my_shape]
        if WINNER_MAPPER[opponent_shape] == my_shape:
            total_points += GAME_PTS_RESULT["WIN"]
        elif opponent_shape == my_shape:
            total_points += GAME_PTS_RESULT["DRAW"]

    return total_points


print(f"Part 1: {main(LINES, engine_part_1)}")
print(f"Part 2: {main(LINES, engine_part_2)}")
