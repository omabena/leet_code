class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) == 0:
            return 0
        
        n = len(height)
        i = 0
        j = n - 1
        max_area = 0
        while i < j:
            area = self.calculate_area(i, j, height)
            if area > max_area:
                max_area = area

            if height[i] < height[j]:
                i = i + 1
            else:
                j = j - 1

        return max_area 


    def calculate_area(self, i, j, height):
        left = height[i]
        right = height[j]
        h = min(left, right)
        base = j - i
        return h * base
