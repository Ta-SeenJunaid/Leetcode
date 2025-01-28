class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        rlen = len(grid)
        clen = len(grid[0])
        max_fish = 0
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rlen or c >= clen or grid[r][c]==0:
                return 0
            temp = grid[r][c]
            grid[r][c] = 0
            return temp + dfs(r+1,c) + dfs(r-1,c) + dfs(r, c+1) + dfs(r, c-1)
        for r in range(rlen):
            for c in range(clen):
                if grid[r][c] != 0:
                    max_fish = max(max_fish, dfs(r,c))
        return max_fish
             
        
