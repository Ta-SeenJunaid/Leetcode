class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle)==1:
            return triangle[0][0]
        pre, cur = triangle[-1], [0 for _ in range(len(triangle[-1]))]
        for row in range(len(triangle)-2, -1, -1):
            for col in range(row, -1, -1):
                cur[col] = min(triangle[row][col] + pre[col], triangle[row][col] + pre[col+1])
            pre = cur
            cur = [0 for _ in range(len(triangle[-1]))]
        return pre[0]
      
