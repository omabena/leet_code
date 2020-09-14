class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        if x == 0:
            return True
        
        
        if  x % 10 == 0:
            return False

        x_string = str(x)

        if len(set(list(x_string))) == 1:
            return True

        return x_string == x_string[::-1]
        