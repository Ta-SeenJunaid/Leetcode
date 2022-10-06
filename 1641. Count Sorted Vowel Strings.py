# https://leetcode.com/problems/count-sorted-vowel-strings/solutions/1021817/python-3-dynamic-programming-explained/

class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [1]*5
        for i in range(n):
            for j in range(1, 5):
                dp[j] += dp[j-1]
        return dp[-1]


solution = Solution()
print(solution.countVowelStrings(n = 1))
print(solution.countVowelStrings(n = 2))
print(solution.countVowelStrings(n = 33))