class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_temp = [temp.lower() for temp in s if temp.isalnum()]
        return s_temp == s_temp[::-1]


solution = Solution()
print(solution.isPalindrome(s = "A man, a plan, a canal: Panama"))
print(solution.isPalindrome(s = "race a car"))
print(solution.isPalindrome(s = " "))