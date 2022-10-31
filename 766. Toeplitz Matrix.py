from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        len_row, len_col = len(matrix), len(matrix[0])
        for i in range(1, len_row):
            for j in range(1, len_col):
                if matrix[i-1][j-1] != matrix[i][j]:
                    return False
        return True


solution = Solution()
print(solution.isToeplitzMatrix(matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]))
print(solution.isToeplitzMatrix(matrix = [[1,2],[2,2]]))