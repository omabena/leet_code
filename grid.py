class Solution(object):
    def numDistinctIslands2(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.find_groups(grid)
    
    def find_groups(self, grid):
        for i, v in enumerate(grid):
            print(i)
            print(v)


grid = [
    [1,1,0,0,0],
    [1,0,0,0,0],
    [0,0,0,0,1],
    [0,0,0,1,1]
]
s = Solution()
s.numDistinctIslands2(grid)