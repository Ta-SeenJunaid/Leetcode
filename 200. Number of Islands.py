from typing import List


class Solution:
    def __init__(self):
        self.grid = None
        self.row = 0
        self.col = 0
        self.visited = set()

    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.row = len(grid)
        self.col = len(grid[0])
        num_of_islands = 0
        for i in range(self.row):
            for j in range(self.col):
                num_of_islands += self.dfs_helper(i,j)
        return num_of_islands

    def dfs_helper(self, r,c):
        if r < 0 or r >= self.row or c < 0 or c >= self.col or self.grid[r][c] == "0" or (r,c) in self.visited:
            return 0
        self.visited.add((r,c))
        self.dfs_helper(r+1,c)
        self.dfs_helper(r-1,c)
        self.dfs_helper(r,c+1)
        self.dfs_helper(r,c-1)
        return 1


solution = Solution()
# print(solution.numIslands(grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]))
print(solution.numIslands(grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))