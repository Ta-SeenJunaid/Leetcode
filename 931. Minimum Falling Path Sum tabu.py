class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        tab = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        tab[0] = matrix[0]
        for row in range(1, len(matrix)):
            for col in range(len(matrix[0])):
                tab[row][col] = min(matrix[row][col] + tab[row-1][col-1] if col > 0 else float('inf'), \
                matrix[row][col] + tab[row-1][col], \
                matrix[row][col] + tab[row-1][col+1] if col < len(matrix[0])-1 else float('inf'))
        return min(tab[-1])
