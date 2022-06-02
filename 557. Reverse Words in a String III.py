class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()
        s=[word[::-1] for word in s]
        return ' '.join(s)


solution = Solution()
print(solution.reverseWords(s = "Let's take LeetCode contest"))
print(solution.reverseWords(s = "God Ding"))