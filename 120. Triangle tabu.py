class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle)==1:
            return triangle[0][0]
        tab = [[0 for _ in range(len(triangle[-1]))] for _ in range(len(triangle))]
        tab[len(triangle)-1] = triangle[-1]
        for row in range(len(triangle)-2, -1, -1):
            for col in range(row, -1, -1):
                tab[row][col] = min(triangle[row][col] + tab[row+1][col], triangle[row][col] + tab[row+1][col+1])
        return tab[0][0]
