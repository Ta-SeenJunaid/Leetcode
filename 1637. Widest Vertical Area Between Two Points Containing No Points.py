from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        max_ = 0
        for i in range(len(points)-1):
            temp = abs(points[i][0]-points[i+1][0])
            if temp >max_:
                max_ = temp
        return max_


solution = Solution()
print(solution.maxWidthOfVerticalArea(points = [[8,7],[9,9],[7,4],[9,7]]))
print(solution.maxWidthOfVerticalArea(points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]))
