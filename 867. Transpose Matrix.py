from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return list(map(list, zip(*matrix)))

solution = Solution()
print(solution.transpose(matrix = [[1,2,3],[4,5,6],[7,8,9]]))
print(solution.transpose([[1,2,3],[4,5,6]]))
