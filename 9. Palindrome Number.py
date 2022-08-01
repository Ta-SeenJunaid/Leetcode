class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        return False


solution = Solution()
print(solution.isPalindrome(x = 121))
print(solution.isPalindrome(x = -121))
print(solution.isPalindrome(x = 10))

