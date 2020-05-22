import time

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        return self._window_strategy(s)
    
    def _is_palindrome(self, s):
        if len(s) > 1 and s[-1] != s[0]:
            return False
        return s[::-1] == s


    def _window_strategy(self, s):
        ## This is a bruteforce implementation with
        ## using some strategies to reduce the number of computations
        i = 0
        j = 1
        n = len(s)
        output = s[0:1]

        if len(set(s)) == 1:
            return s

        while (i < j and j < n and i < n):
            j = j + 1
            window = s[i:j]
            if len(output) > len(window):
                break
            
            if (self._is_palindrome(window)
                and len(window) > len(output)):
                output = window

            if j == n:
                i = i + 1
                j = i + len(output)

        return output
