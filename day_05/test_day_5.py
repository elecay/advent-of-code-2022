import unittest
from unittest import TestCase

from day_05.day import engine_part_1, engine_part_2
from utils import main, read_file

LINES = read_file("day_05/example.txt")


class TestDay(TestCase):
    def test_example(self):
        self.assertEqual(main(LINES, engine_part_1), "CMZ")

    @unittest.skip
    def test_example_part_2(self):
        self.assertEqual(main(LINES, engine_part_2), 4)
