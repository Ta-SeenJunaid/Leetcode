class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 0, num
        while left<=right:
            mid = (left+right)//2
            temp = mid*mid
            if temp==num:
                return True
            elif temp>num:
                right=mid-1
            else:
                left=mid+1


solution = Solution()
print(solution.isPerfectSquare(num = 16))
print(solution.isPerfectSquare(num = 14))
print(solution.isPerfectSquare(num = 9))