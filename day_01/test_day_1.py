from unittest import TestCase

from day_01.day import engine_part_1
from utils import main, read_file

LINES = read_file("day_01/example.txt")


class TestDay(TestCase):
    def test_example(self):
        self.assertEqual(main(LINES, engine_part_1), 24_000)
