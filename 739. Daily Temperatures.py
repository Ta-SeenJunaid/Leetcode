# https://www.youtube.com/watch?v=cTBiBSnjO3c
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                index, _ = stack.pop()
                result[index] = i-index
            stack.append([i, temp])
        return result


solution = Solution()
print(solution.dailyTemperatures(temperatures = [73,74,75,71,69,72,76,73]))
print(solution.dailyTemperatures(temperatures = [30,40,50,60]))
print(solution.dailyTemperatures(temperatures = [30,60,90]))