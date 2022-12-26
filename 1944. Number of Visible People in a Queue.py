# https://www.youtube.com/watch?v=nzRG4dV4F_8
from typing import List

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        heights_len = len(heights)
        result = [0]*heights_len
        stack = []
        for i in range(heights_len-1, -1, -1):
            visible = 0
            while stack and heights[i]>stack[-1]:
                stack.pop()
                visible += 1
            if stack:
                visible += 1
            stack.append(heights[i])
            result[i] = visible
        return result


solution = Solution()
print(solution.canSeePersonsCount(heights = [10,6,8,5,11,9]))
print(solution.canSeePersonsCount(heights = [5,1,2,3,10]))
