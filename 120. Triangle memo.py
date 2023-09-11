class Solution:
    def __init__(self):
        self.memo = None

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle)==1:
            return triangle[0][0]
        self.memo = [[-1 for _ in range(len(triangle[-1]))] for _ in range(len(triangle))]
        return self.dp_re(triangle, 0, 0)
    
    def dp_re(self, triangle, row, col):
        if row == len(triangle) - 1:
            return triangle[row][col]
        if self.memo[row][col] != -1:
            return self.memo[row][col]
        self.memo[row][col] = min((triangle[row][col] + self.dp_re(triangle, row+1, col)),\
        (triangle[row][col] + self.dp_re(triangle, row+1, col+1)))
        return self.memo[row][col]
      
