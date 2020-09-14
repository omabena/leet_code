import re

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """ 
        m = re.match(r'\s*([-,+]{0,1}[0-9]*)', str)

        if len(m.group(1)) == 0:
            return 0

        try:
            num = int(m.group(1))
        except Exception:
            return 0
        

        if num > 2**31 -1:
            return 2147483647 
        if num < -2**31:
            return -2147483648

        return num
        

