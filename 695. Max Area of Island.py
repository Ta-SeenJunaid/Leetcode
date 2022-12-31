# https://www.youtube.com/watch?v=iJGr1OtmH0c
from typing import List


class Solution:
    def __init__(self):
        self.visited = set()
        self.row = 0
        self.col = 0
        self.grid = None

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.row = len(grid)
        self.col = len(grid[0])
        max_area = 0
        for i in range(self.row):
            for j in range(self.col):
                max_area = max(max_area, self.dfs_helper(i,j))
        return max_area


    def dfs_helper(self, r, c):
        if r < 0 or r >= self.row or c < 0 or c >= self.col or self.grid[r][c] == 0 or (r,c) in self.visited:
            return 0
        self.visited.add((r,c))
        return 1 + self.dfs_helper(r+1, c) + self.dfs_helper(r-1, c)\
            + self.dfs_helper(r, c+1) + self.dfs_helper(r, c-1)


solution = Solution()
print(solution.maxAreaOfIsland(grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],
                                 [0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],
                                 [0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))
print(solution.maxAreaOfIsland(grid = [[0,0,0,0,0,0,0,0]]))