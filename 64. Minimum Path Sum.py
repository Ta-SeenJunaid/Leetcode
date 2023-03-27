# https://www.youtube.com/watch?v=hwRWt-PH394
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if row == 0 and col != 0:
                    grid[row][col] += grid[row][col-1]
                elif col == 0 and row != 0:
                    grid[row][col] += grid[row-1][col]
                elif row != 0 and col != 0:
                    grid[row][col] += min(grid[row-1][col], grid[row][col-1])
        return grid[-1][-1]


solution = Solution()
print(solution.minPathSum(grid = [[1,3,1],[1,5,1],[4,2,1]]))
print(solution.minPathSum(grid = [[1,2,3],[4,5,6]]))