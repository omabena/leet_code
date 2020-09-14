import unittest
from src.moving_average import MovingAverage


class TestMovingAverage(unittest.TestCase):

    def setUp(self):
        self.movingAverage = None

    def test_base_case(self):
        self.movingAverage = MovingAverage(size=3)
        self.assertEqual(self.movingAverage.next(1), 1)
        self.assertEqual(self.movingAverage.next(5), 3)
        self.assertEqual(self.movingAverage.next(8), 4.666666666666667)
        self.assertEqual(self.movingAverage.next(10), 7.666666666666667)

    def test_size_1_queue(self):
        self.movingAverage = MovingAverage(size=1)
        self.assertEqual(self.movingAverage.next(4), 4)
        self.assertEqual(self.movingAverage.next(0), 0)


if __name__ == '__main__':
    unittest.main()
