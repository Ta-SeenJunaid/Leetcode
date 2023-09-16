class Solution:
    def __init__(self):
        self.memo = None

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        self.memo = [[-1.1 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        ans = float('inf')
        for idx in range(len(matrix[0])):
            ans = min(ans, self.dp_re(matrix, len(matrix)-1, idx))
        return ans

    def dp_re(self, matrix: List[List[int]], row, col):     
        if col < 0 or col >= len(matrix[0]):
            return float('inf')
        elif row == 0:
            return matrix[row][col]
        elif self.memo[row][col] != -1.1:
            return self.memo[row][col] 
        self.memo[row][col] = min(matrix[row][col] + self.dp_re(matrix, row-1, col-1), matrix[row][col] + self.dp_re(matrix, row-1, col), \
        matrix[row][col] + self.dp_re(matrix, row-1, col+1))
        return self.memo[row][col]
