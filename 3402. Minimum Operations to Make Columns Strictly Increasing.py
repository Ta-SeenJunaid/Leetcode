class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        ans = 0
        if len(grid) == 1:
            return ans
        for row in range(1,len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] <= grid[row-1][col]:
                    temp = grid[row-1][col] - grid[row][col] + 1
                    ans += temp
                    grid[row][col] += temp
        return ans
        
