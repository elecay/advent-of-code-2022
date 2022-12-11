from unittest import TestCase

from day import main


class TestDay1(TestCase):
    def test_example(self):
        self.assertEqual(main(1), 24_000)
