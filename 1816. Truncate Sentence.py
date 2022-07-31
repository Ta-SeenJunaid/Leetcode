class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return ' '.join(s.split()[:k])


solution = Solution()
print(solution.truncateSentence(s = "Hello how are you Contestant", k = 4))
print(solution.truncateSentence(s = "What is the solution to this problem", k = 4))
print(solution.truncateSentence(s = "chopper is not a tanuki", k = 5))
