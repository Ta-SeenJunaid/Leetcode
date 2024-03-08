class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        g_len = len(grid)
        temp = [[0 for _ in range(g_len)] for _ in range(g_len)]
        ans = 0
        for i in range(g_len):
            for j in range(g_len):
                ans += max(grid[i][j], min(max(grid[i]), max(grid[k][j] for k in range(g_len)))) - grid[i][j]  
        return ans
        
