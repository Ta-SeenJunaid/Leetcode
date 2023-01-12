from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        result = [[0]*(n-2) for _ in range(n-2)]
        for i in range(0, n-2):
            for j in range(0, n-2):
                result[i][j] = max(grid[ii][jj] for ii in range(i, i+3) for jj in range(j, j+3))
        return result


solution = Solution()
print(solution.largestLocal(grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]))
print(solution.largestLocal(grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]))