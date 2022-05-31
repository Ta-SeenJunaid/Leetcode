# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 0, n
        while left<=right:
            mid = (left+right) // 2
            if isBadVersion(mid) == False and isBadVersion(mid+1) == True:
                return mid+1
            elif isBadVersion(mid) == True and isBadVersion(mid-1) == False:
                return mid
            elif isBadVersion(mid)==True and isBadVersion(mid-1) == True:
                right = mid - 1
            else:
                left = mid + 1




