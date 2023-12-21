from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x:x[0])
        #points.sort()
        ans = 0
        for i in range(len(points)-1):
            ans = max(ans, points[i+1][0] - points[i][0])
        return ans


solution = Solution()
print(solution.maxWidthOfVerticalArea(points = [[8,7],[9,9],[7,4],[9,7]]))
print(solution.maxWidthOfVerticalArea(points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]))
