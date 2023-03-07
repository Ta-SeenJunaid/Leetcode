# https://www.youtube.com/watch?v=yXwLmfLnhko
from typing import List


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        time.sort()
        l, r = time[0], time[-1]*totalTrips
        ans = r
        while l <= r:
            mid = (l+r)//2
            temp = 0
            for i in time:
                temp += mid//i
                if temp >= totalTrips:
                    break
            if temp>=totalTrips:
                ans = mid
                r = mid-1
            else:
                l = mid+1
        return ans



solution = Solution()
print(solution.minimumTime(time = [1,2, 3], totalTrips = 5))
print(solution.minimumTime(time = [2], totalTrips = 1))

