import math
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if numRows == 1:
            return s

        if numRows >= len(s):
            return s

        n = len(s)
        cols = int(math.ceil(n/float(numRows)))
        offset = numRows - 2

        if offset == 0:
            M = self.zeros_matrix(numRows, cols)
        else:
            M = self.zeros_matrix(numRows, len(s))

        # Choose al columns
        col_letters = 0
        end_letter = numRows
        col_current = 0
        i = 0

        while i in range(cols):
            if col_letters < n:
                letters_column = s[col_letters : end_letter]
            else:
                letters_column= s[col_letters:]
            
            diag_letters = s[end_letter: end_letter + offset]
            if len(letters_column) == 0:
                break

            for row in range(len(letters_column)):
                M[row][col_current] = letters_column[row]
            
            row_diag = offset
            col_diag = col_current
            row_diag_letter = 0
            while (row_diag >= 1 
                    and len(diag_letters) > 0 
                    and row_diag_letter < len(diag_letters)):
                col_diag = col_diag + 1
                M[row_diag][col_diag] = diag_letters[row_diag_letter]
                row_diag = row_diag - 1
                row_diag_letter = row_diag_letter  + 1

            col_letters += (numRows + offset)
            end_letter += (numRows + offset)
            col_current = col_current + 1 + offset
            
            i = i + 1 
        s = self.convert_matrix(M)
        return s

    def convert_matrix(self, M):
        """
        Print a matrix one row at a time
            :param M: The matrix to be printed
        """
        r = ''
        for row in M:
            r += ''.join([x for x in row if x != 0.0])
        return r

 
    def zeros_matrix(self, rows, cols):
        """
        Creates a matrix filled with zeros.
            :param rows: the number of rows the matrix should have
            :param cols: the number of columns the matrix should have
            :return: list of lists that form the matrix
        """
        M = []
        while len(M) < rows:
            M.append([])
            while len(M[-1]) < cols:
                M[-1].append(0.0)
    
        return M