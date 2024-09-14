# https://www.youtube.com/watch?v=zMqgIbLLsc4&list=LL&index=2

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        def dfs_helper(r, c, matrix):
            if r < 0 or c < 0 or r >= len(matrix) or c >= len(matrix[0]) or matrix[r][c] == 1:
                return
            matrix[r][c] = 1
            dfs_helper(r-1, c, matrix)
            dfs_helper(r+1, c, matrix)
            dfs_helper(r, c+1, matrix)
            dfs_helper(r, c-1, matrix) 
        
        regions = 0
        row = len(grid)
        col = len(grid[0])
        matrix = [[0 for _ in range(col*3)] for _ in range(row*3)]
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "\\":
                    matrix[r*3][c*3] = 1
                    matrix[r*3+1][c*3+1] = 1
                    matrix[r*3+2][c*3+2] = 1
                elif grid[r][c] == "/":
                    matrix[r*3][c*3+2] = 1
                    matrix[r*3+1][c*3+1] = 1
                    matrix[r*3+2][c*3] = 1
        
        for r in range(row*3):
            for c in range(col*3):
                if matrix[r][c] == 0:
                    regions += 1
                    dfs_helper(r, c, matrix)
        return regions


        
