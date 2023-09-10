class Solution:    
    def minPathSum(self, grid: List[List[int]]) -> int:
        pre, cur = [float('inf') for _ in range(len(grid[0]))], [float('inf') for _ in range(len(grid[0]))]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if row == 0 and col == 0:
                    cur[0] = grid[row][col]
                else:
                    cur[col] = min((grid[row][col]+(cur[col-1] if col > 0 else float('inf'))), \
                    (grid[row][col]+ pre[col]))
            pre = cur
        return cur[-1]
      
