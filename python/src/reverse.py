class Solution:
    def reverse(self, x: int) -> int:
        num = int(str(abs(x))[::-1])
        if num > 2**31 -1:
            return 0
        
        if x < 0:
            return -1*num
        else:
            return num

s = Solution()
reverse_int = s.reverse(270892374)
print(reverse_int)