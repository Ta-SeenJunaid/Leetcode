class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])


solution = Solution()
print(solution.reverseWords(s = "the sky is blue"))
print(solution.reverseWords(s = "  hello world  "))
print(solution.reverseWords(s = "a good   example"))