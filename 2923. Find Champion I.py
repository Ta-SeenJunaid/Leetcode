class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        row_len = len(grid[0])
        for i in range(len(grid)):
            if sum(grid[i]) == row_len-1:
                return i
        
