from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if k < arr[0]:
            return k
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = (l+r) // 2
            if arr[mid] - (mid + 1) < k:
                l = mid + 1
            else:
                r = mid - 1
        return l+k



solution = Solution()
print(solution.findKthPositive(arr = [2,3,4,7,11], k = 5))
print(solution.findKthPositive(arr = [1,2,3,4], k = 2))
