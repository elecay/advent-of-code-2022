from unittest import TestCase

from day_04.day import engine_part_1, engine_part_2
from utils import main, read_file

LINES = read_file("day_04/example.txt")


class TestDay(TestCase):
    def test_example(self):
        self.assertEqual(main(LINES, engine_part_1), 2)

    def test_example_part_2(self):
        self.assertEqual(main(LINES, engine_part_2), 4)
