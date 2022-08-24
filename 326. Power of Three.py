class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        while n % 3 == 0:
            n /= 3
        return n == 1


solution = Solution()
print(solution.isPowerOfThree(n = 27))
print(solution.isPowerOfThree(n = 0))
print(solution.isPowerOfThree(n = 9))
