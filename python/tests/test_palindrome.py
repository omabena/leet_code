import unittest
from src.palindrome import Solution

class TestPalindrome(unittest.TestCase):

    palindrome = None

    def setUp(self):
        self.palindrome = Solution()


    def test_base_case(self):
        s = 'babad'
        output = self.palindrome.longestPalindrome(s)
        self.assertEqual(output, 'bab')

        s = 'cbbd'
        output = self.palindrome.longestPalindrome(s)
        self.assertEqual(output, 'bb')


    def test_single_letter(self):
        s = 'c'
        output = self.palindrome.longestPalindrome(s)
        self.assertEqual(output, 'c')


    def test_two_equals_letters(self):
        s = 'cc'
        output = self.palindrome.longestPalindrome(s)
        self.assertEqual(output, 'cc')


    def test_empty_string(self):
        s = ''
        output = self.palindrome.longestPalindrome(s)
        self.assertEqual(output, '')


    def test_all_different_letters(self):
        s = 'abcdefg'
        output = self.palindrome.longestPalindrome(s)
        self.assertEqual(output, 'a')


    def test_only_diffent_letter_middle(self):
        s = 'cccaccc'
        output = self.palindrome.longestPalindrome(s)
        self.assertEqual(output, 'cccaccc')


    def test_long_single_letter(self):
        s = 'cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc'
        output = self.palindrome.longestPalindrome(s)
        self.assertEqual(output, s)


    def test_edge_4_letters_not_solution(self):
        s = 'aaaabaaa'
        output = self.palindrome.longestPalindrome(s)
        self.assertEqual(output, 'aaabaaa')


    def test_long_different_letters(self):
        s = 'gphyvqruxjmwhonjjrgumxjhfyupajxbjgthzdvrdqmdouuukeaxhjumkmmhdglqrrohydrmbvtuwstgkobyzjjtdtjroqpyusfsbjlusekghtfbdctvgmqzeybnwzlhdnhwzptgkzmujfldoiejmvxnorvbiubfflygrkedyirienybosqzrkbpcfidvkkafftgzwrcitqizelhfsruwmtrgaocjcyxdkovtdennrkmxwpdsxpxuarhgusizmwakrmhdwcgvfljhzcskclgrvvbrkesojyhofwqiwhiupujmkcvlywjtmbncurxxmpdskupyvvweuhbsnanzfioirecfxvmgcpwrpmbhmkdtckhvbxnsbcifhqwjjczfokovpqyjmbywtpaqcfjowxnmtirdsfeujyogbzjnjcmqyzciwjqxxgrxblvqbutqittroqadqlsdzihngpfpjovbkpeveidjpfjktavvwurqrgqdomiibfgqxwybcyovysydxyyymmiuwovnevzsjisdwgkcbsookbarezbhnwyqthcvzyodbcwjptvigcphawzxouixhbpezzirbhvomqhxkfdbokblqmrhhioyqubpyqhjrnwhjxsrodtblqxkhezubprqftrqcyrzwywqrgockioqdmzuqjkpmsyohtlcnesbgzqhkalwixfcgyeqdzhnnlzawrdgskurcxfbekbspupbduxqxjeczpmdvssikbivjhinaopbabrmvscthvoqqbkgekcgyrelxkwoawpbrcbszelnxlyikbulgmlwyffurimlfxurjsbzgddxbgqpcdsuutfiivjbyqzhprdqhahpgenjkbiukurvdwapuewrbehczrtswubthodv'
        output = self.palindrome.longestPalindrome(s)
        self.assertEqual(output, 'jtdtj')


if __name__ == '__main__':
    unittest.main()
