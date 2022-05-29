class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left <= right:
            mid = (left+right)//2
            temp = mid*mid
            if temp==x or temp < x < (mid + 1)*(mid + 1):
                return mid
            elif temp > x:
                right=mid-1
            else:
                left=mid+1


solution = Solution()
print(solution.mySqrt(x=4))
print(solution.mySqrt(x=8))