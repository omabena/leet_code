import unittest
from src.lasgest_time_from_digits import Solution


class TestLargestTimeFromDigits(unittest.TestCase):

    solution = None

    def setUp(self):
        self.solution = Solution()

    def test_base_case(self):
        output = self.solution.largestTimeFromDigits([1, 2, 3, 4])
        self.assertEqual(output, "23:41")

    def test_empty_not_valid_first_number(self):
        output = self.solution.largestTimeFromDigits([4, 9, 3, 5])
        self.assertEqual(output, "")

    def test_valid_first_number(self):
        output = self.solution.largestTimeFromDigits([4, 9, 1, 5])
        self.assertEqual(output[0], "1")

    def test_valid_second_number(self):
        output = self.solution.largestTimeFromDigits([4, 9, 1, 5])
        self.assertEqual(output[0], "1")
        self.assertEqual(output[1], "9")

    def test_valid_third_number(self):
        output = self.solution.largestTimeFromDigits([4, 9, 1, 5])
        self.assertEqual(output[0], "1")
        self.assertEqual(output[1], "9")
        self.assertEqual(output[2], ":")
        self.assertEqual(output[3], "5")

    def test_valid_fourth_number(self):
        output = self.solution.largestTimeFromDigits([4, 9, 1, 5])
        self.assertEqual(output[0], "1")
        self.assertEqual(output[1], "9")
        self.assertEqual(output[2], ":")
        self.assertEqual(output[3], "5")
        self.assertEqual(output[4], "4")

    def test_zero_first_number(self):
        output = self.solution.largestTimeFromDigits([2, 0, 6, 6])
        self.assertEqual(output[0], "06:26")
