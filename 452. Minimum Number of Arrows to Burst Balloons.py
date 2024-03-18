class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        ans = 1
        points.sort(key=lambda x: x[1])
        x = points[0][1]
        for i in range(1, len(points)):
            if points[i][0] <= x and points[i][1] >= x:
                continue
            ans += 1
            x = points[i][1]
        return ans
        
