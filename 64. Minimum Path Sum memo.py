class Solution:
    def __init__(self):
        self.memo = None

    def minPathSum(self, grid: List[List[int]]) -> int:
        self.memo = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        return self.dp_re(grid, len(grid)-1, len(grid[0])-1)
    
    def dp_re(self, grid:List[List[int]], row:int, col:int) -> int:
        if row == 0 and col == 0:
            return grid[row][col]
        if row < 0 or col < 0:
            return float('inf')
        if self.memo[row][col] != -1:
            return self.memo[row][col]
        self.memo[row][col] = min((grid[row][col] + self.dp_re(grid, row - 1, col)),\
         (grid[row][col] + self.dp_re(grid, row, col -1)))
        
        return self.memo[row][col]
        
