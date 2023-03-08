# https://www.youtube.com/watch?v=U2SozAs9RzA
from math import ceil
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ans = r
        while l <= r:
            mid = (l+r)//2
            count = 0
            for i in piles:
                count += ceil(i/mid)
            if count <= h:
                ans = mid
                r = mid -1
            else:
                l = mid + 1
        return ans


solution = Solution()
print(solution.minEatingSpeed(piles = [3,6,7,11], h = 8))
print(solution.minEatingSpeed(piles = [30,11,23,4,20], h = 5))
print(solution.minEatingSpeed(piles = [30,11,23,4,20], h = 6))