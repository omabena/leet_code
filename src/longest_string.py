class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = i = j = 0
        n = len(s)
        set_acc = set()
        while(i < n and j < n):
            if s[j] not in set_acc:
                set_acc.add(s[j])
                j = j + 1
                ans = max(ans, j - i)
            else:
                set_acc.remove(s[i])
                i = i + 1
                
        return ans
