class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        tab = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if row == 0 and col == 0:
                    tab[row][col] = grid[row][col]
                else:
                    tab[row][col] = min((grid[row][col] + (tab[row-1][col] if row > 0 else float('inf'))),\
                     (grid[row][col] + (tab[row][col-1] if col > 0 else float('inf'))))
        return tab[-1][-1]
        
