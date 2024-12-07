# https://leetcode.com/problems/fixed-point/editorial
class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        ans = -1
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = (left+right)//2
            if arr[mid] == mid:
                ans = mid
                right = mid - 1
            if arr[mid] < mid:
                left = mid + 1
            else:
                right = mid - 1
        return ans
        
