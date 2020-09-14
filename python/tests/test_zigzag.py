import unittest
from src.zigzag import Solution

class TestZigZag(unittest.TestCase):
    zigzag = None

    def setUp(self):
        self.zigzag = Solution()
    

    def test_base_case(self):
        self.assertIsNotNone(self.zigzag)
        convertion = self.zigzag.convert("PAYPALISHIRING", 3)
        self.assertEqual(convertion, "PAHNAPLSIIGYIR")

    def test_base_case_4_rows(self):
        self.assertIsNotNone(self.zigzag)
        convertion = self.zigzag.convert("PAYPALISHIRING", 4)
        self.assertEqual(convertion, "PINALSIGYAHRPI")


    def test_case_1_row(self):
        self.assertIsNotNone(self.zigzag)
        convertion = self.zigzag.convert("AB", 1)
        self.assertEqual(convertion, "AB")

    def test_length_string_close_to_rows(self):
        self.assertIsNotNone(self.zigzag)
        convertion = self.zigzag.convert("ABCDE", 4)
        self.assertEqual(convertion, "ABCED")

    def test_length_no_diags(self):
        self.assertIsNotNone(self.zigzag)
        convertion = self.zigzag.convert("PAYPALISHIRING", 2)
        self.assertEqual(convertion, "PYAIHRNAPLSIIG") 


    def test_rows_more_than_letters(self):
        self.assertIsNotNone(self.zigzag)
        convertion = self.zigzag.convert("A", 2)
        self.assertEqual(convertion, "A") 

    def test_rows_no_diags_odd_letters(self):
        self.assertIsNotNone(self.zigzag)
        convertion = self.zigzag.convert("ABC", 2)
        self.assertEqual(convertion, "ACB") 


    def test_with_long_word(self):
        self.assertIsNotNone(self.zigzag)
        convertion = self.zigzag.convert("Apalindromeisaword,phrase,number,orothersequenceofunitsthatcanbereadthesamewayineitherdirection,withgeneralallowancesforadjustmentstopunctuationandworddividers.", 3)
        self.assertEqual(convertion, "Aiosrhem,tseoihartaaeeriwgrlasasnoctaoieplnrmiaodprs,ubroohreunefnttacneedhsmwynihrieto,iheeaalwnefrdutettpntainnwrdvdr.adew,anereqcustbaeeitdcntnlocojmsuuoddis") 

    def test_matrix_dimensions(self):
        M = self.zigzag.zeros_matrix(3, 4)
        self.assertEqual(len(M), 3)
        self.assertEqual(len(M[0]), 4)


if __name__ == '__main__':
    unittest.main()