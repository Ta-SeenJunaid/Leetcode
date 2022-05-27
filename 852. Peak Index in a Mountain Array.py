from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr)-1
        while left < right:
            mid = (left+right)//2
            if arr[mid]<arr[mid+1]:
                left=mid+1
            else:
                right=mid
        return right
        # return lef will be ok too


solution = Solution()
print(solution.peakIndexInMountainArray(arr = [0,1,0]))
print(solution.peakIndexInMountainArray(arr = [0,2,1,0]))
print(solution.peakIndexInMountainArray(arr = [0,10,5,2]))
print(solution.peakIndexInMountainArray(arr = [3,9,8,6,4]))