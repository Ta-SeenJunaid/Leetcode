# https://leetcode.com/problems/remove-palindromic-subsequences/solutions/490317/python-3-one-line-beats-100/

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        return 1 if s == s[::-1] else 2


solution = Solution()
print(solution.removePalindromeSub(s = "ababa"))
print(solution.removePalindromeSub(s = "abb"))
print(solution.removePalindromeSub(s = "baabb"))