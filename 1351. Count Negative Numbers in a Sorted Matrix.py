from typing import List


# class Solution:
#     def countNegatives(self, grid: List[List[int]]) -> int:
#         count = 0
#         for i in grid:
#             for j in i[::-1]:
#                 if j < 0:
#                     count +=1
#                 else:
#                     break
#         return count

#https://www.youtube.com/watch?v=-PaWC4MU7_Y
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        row_len = len(grid)
        col_len = len(grid[0])

        i = 0
        j = col_len-1

        while i < row_len and j >=0:
            if grid[i][j] < 0:
                count +=row_len-i
                j -= 1
            else:
                i +=1
        return count


solution = Solution()
print(solution.countNegatives(grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))
print(solution.countNegatives(grid = [[3,2],[1,0]]))
print(solution.countNegatives(grid = [[5,1,0],[-5,-5,-5]]))


