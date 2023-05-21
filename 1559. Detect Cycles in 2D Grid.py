from typing import List


class Solution:
    def __init__(self):
        self.visited = set()
        self.r_len = 0
        self.c_len = 0
    def containsCycle(self, grid: List[List[str]]) -> bool:
        self.r_len = len(grid)
        self.c_len = len(grid[0])
        for i in range(self.r_len):
            for j in range(self.c_len):
                if (i, j) not in self.visited:
                    temp = self.dfs(i, j, (-1, -1), grid)
                    if temp:
                        return True
        return False

    def dfs(self, r, c, parent, grid):
        # print(r, c)
        self.visited.add((r, c))
        up = down = right = left = False
        if (r-1) >= 0 and grid[r-1][c] == grid[r][c] and (r-1, c) in self.visited and (r-1, c) != parent:
            # up = True
            return True
        elif (r-1) >= 0 and grid[r-1][c] == grid[r][c] and (r-1, c) not in self.visited:
            up = self.dfs(r-1, c, (r,c), grid)

        if (r+1) < self.r_len and grid[r+1][c] == grid[r][c] and (r+1, c) in self.visited and (r+1, c) != parent:
            # down = True
            return True
        elif (r+1) < self.r_len and grid[r+1][c] == grid[r][c] and (r+1, c) not in self.visited:
            down = self.dfs(r+1, c, (r,c), grid)

        if (c-1) >= 0 and grid[r][c-1] == grid[r][c] and (r, c-1) in self.visited and (r, c-1) != parent:
            # left = True
            return True
        elif (c-1) >= 0 and grid[r][c-1] == grid[r][c] and (r, c-1) not in self.visited:
            left = self.dfs(r, c-1, (r,c), grid)

        if (c+1) < self.c_len and grid[r][c+1] == grid[r][c] and (r, c+1) in self.visited and (r, c+1) != parent:
            # right = True
            return True
        elif (c+1) < self.c_len and grid[r][c+1] == grid[r][c] and (r, c+1) not in self.visited:
            right = self.dfs(r, c+1, (r,c), grid)

        # print(r, c, parent, up, down, left, right)
        return up or down or left or right


solution = Solution()
print(solution.containsCycle(grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]))

solution = Solution()
print(solution.containsCycle(grid = [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]))

solution = Solution()
print(solution.containsCycle(grid = [["a","b","b"],["b","z","b"],["b","b","a"]]))

solution = Solution()
print(solution.containsCycle(grid = [["c","a","d"],["a","a","a"],["a","a","d"],["a","c","d"],["a","b","c"]]))