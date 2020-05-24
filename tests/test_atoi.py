import unittest
from src.atoi import Solution

class TestAtoi(unittest.TestCase):

    atoi = None

    def setUp(self):
        self.atoi = Solution()

    def test_base_case(self):
        output = self.atoi.myAtoi("0")
        self.assertEqual(output, 0)

    
    def test_discard_white(self):
        output = self.atoi.myAtoi("    42")
        self.assertEqual(output, 42)


    def test_int_with_numbers_end(self):
        output = self.atoi.myAtoi("4193 with words")
        self.assertEqual(output, 4193)

    
    def test_int_with_numbers_beginning(self):
        output = self.atoi.myAtoi("words and 987")
        self.assertEqual(output, 0)


    def test_int_with_sign(self):
        output = self.atoi.myAtoi("-4193")
        self.assertEqual(output, -4193)
    

    def test_int_number_out_of_range(self):
        output = self.atoi.myAtoi("-91283472332")
        self.assertEqual(output, -2147483648)


    def test_string_only_sign(self):
        output = self.atoi.myAtoi("-")
        self.assertEqual(output, 0)


    def test_sitring_plus_sign(self):
        output = self.atoi.myAtoi("+1")
        self.assertEqual(output, 1)
if __name__ == '__main__':
    unittest.main()