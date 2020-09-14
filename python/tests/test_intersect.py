import unittest
from src.intersect import Solution

class TestIntersect(unittest.TestCase): 

    solution = Solution()

    def setUp(self):
        self.solution = Solution()


    def test_base_case(self):
        nums1 = [1, 2, 2, 1]
        nums2 = [2, 2]
        output = self.solution.intersect(nums1, nums2)
        self.assertEqual(output, [2, 2])

        nums1 = [4,9,5]
        nums2 = [9,4,9,8,4]
        output = self.solution.intersect(nums1, nums2)
        self.assertEqual(output, [4, 9])

    def test_empty_list(self):
        nums1 = []
        nums2 = [2, 2]
        output = self.solution.intersect(nums1, nums2)
        self.assertEqual(output, [])

    def test_list_less_numbers(self):
        nums1 = [1, 2]
        nums2 = [1, 1]
        output = self.solution.intersect(nums1, nums2)
        self.assertEqual(output, [1])

if __name__ == '__main__':
    unittest.main()