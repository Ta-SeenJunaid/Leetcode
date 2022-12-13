from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum = 0
        mat_len = len(mat)
        for i in range(mat_len):
            sum +=mat[i][i] + mat[mat_len-1-i][i]
        if mat_len%2 != 0:
            sum -=mat[mat_len//2][mat_len//2]
        return sum



solution = Solution()
print(solution.diagonalSum(mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]))
print(solution.diagonalSum(mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]))
print(solution.diagonalSum(mat = [[5]]))
print(solution.diagonalSum(mat = [[0]]))