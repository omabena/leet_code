import unittest
from src.integer_palindrome import Solution

class TestIntegerPalindrome(unittest.TestCase):

    palindrome = None

    def setUp(self):
        self.palindrome = Solution()


    def test_base_case(self):
        output = self.palindrome.isPalindrome(121)
        self.assertEqual(output, True)


    def test_negative_int(self):
        output = self.palindrome.isPalindrome(-121)
        self.assertEqual(output, False)


    def test_all_numbers_equal(self):
        output = self.palindrome.isPalindrome(555555)
        self.assertEqual(output, True)


    def test_single_number(self):
        output = self.palindrome.isPalindrome(5)
        self.assertEqual(output, True)
    

    def test_no_palindrome(self):
        output = self.palindrome.isPalindrome(293842)
        self.assertEqual(output, False)


    def test_module_10(self):
        output = self.palindrome.isPalindrome(100)
        self.assertEqual(output, False)


    def test_for_zero(self):
        output = self.palindrome.isPalindrome(0)
        self.assertEqual(output, True)

if __name__ == '__main__':
    unittest.main()