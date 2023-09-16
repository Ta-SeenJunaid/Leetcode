class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        pre = matrix[0]
        for row in range(1, len(matrix)):
            cur = [0 for _ in range(len(matrix[0]))]
            for col in range(len(matrix[0])):
                cur[col] = min(matrix[row][col] + pre[col-1] if col > 0 else float('inf'), \
                matrix[row][col] + pre[col], \
                matrix[row][col] + pre[col+1] if col < len(matrix[0])-1 else float('inf'))
            pre = cur
        return min(pre)
