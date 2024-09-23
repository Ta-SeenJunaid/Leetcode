class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs_helper(r, c):
            if r < 0 or r == len(grid) or c < 0 or c == len(grid[0]):
                return
            elif grid[r][c] == 0:
                return
            elif (r, c) not in visited:
                visited.add((r,c))
                for rd, cd in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    dfs_helper(r+rd, c+cd)
        visited = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row == 0 or col == 0 or row == len(grid)-1 or col == len(grid[0])-1) and grid[row][col] == 1:
                    dfs_helper(row, col)
        ans = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and (row, col) not in visited:
                    ans += 1
        return ans

        
