from typing import List
from numpy import random


class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        combinations = []

        for i in range(10000):
            x = self.sim(arr)
            combinations.append(x)

        if [1, 2, 3, 4] in combinations:
            print('interesting')

        print(combinations)
        return "23:45"

    def sim(self, arr: List[int]) -> List[int]:
        n = 3
        x = [1, 2, 3, 4]
        k = n
        U = random.uniform(size=1)[0]

        while k > 0:
            i = int(k + 1 * U)
            p_i = x[i]
            p_k = x[k]
            x[i] = p_k
            x[k] = p_i
            k = k - 1
        return x

    def check_is_valid(self, arr: List[int]) -> bool:
        if arr[0] not in [0, 1, 2]:
            return False

        if arr[0] in [0, 1]:
            if arr[1] not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
                return False

        if arr[1] == 2:
            if arr[1] not in [0, 1, 2, 3]:
                return False

        if arr[2] not in [0, 1, 2, 3, 4, 5]:
            return False

        if arr[3] not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return False

        return True


s = Solution()
s.largestTimeFromDigits([0, 1, 2, 3])
