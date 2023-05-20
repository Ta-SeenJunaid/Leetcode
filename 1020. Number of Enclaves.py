from typing import List


class Solution:
    def __init__(self):
        self.visited = set()
        self.r_len = 0
        self.c_len = 0
    def numEnclaves(self, grid: List[List[int]]) -> int:
        self.r_len = len(grid)
        self.c_len = len(grid[0])
        ans = 0
        for j in range(self.c_len):
            if grid[0][j] == 1:
                self.dfs(0, j, grid)
            if grid[self.r_len-1][j] == 1:
                self.dfs(self.r_len-1, j, grid)
        for i in range(1, self.r_len-1):
            if grid[i][0] == 1:
                self.dfs(i, 0, grid)
            if grid[i][self.c_len-1] == 1:
                self.dfs(i, self.c_len-1, grid)
        for i in range(1, self.r_len-1):
            for j in range(1, self.c_len-1):
                if grid[i][j] == 1 and (i, j) not in self.visited:
                    ans += 1
        return ans

    def dfs(self, r, c, grid):
        if r < 0 or r >= self.r_len or c < 0 or c >= self.c_len or (r, c) in self.visited or grid[r][c] == 0:
            return
        self.visited.add((r, c))
        self.dfs(r+1, c, grid)
        self.dfs(r-1, c, grid)
        self.dfs(r, c+1, grid)
        self.dfs(r, c-1, grid)
        return


solution = Solution()
print(solution.numEnclaves(grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]))

solution = Solution()
print(solution.numEnclaves(grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]))

solution = Solution()
print(solution.numEnclaves(grid = [[0],[1],[1],[0],[0]]))