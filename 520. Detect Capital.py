class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper():
            return True
        elif word.islower():
            return True
        elif word[0].isupper() and word[1:].islower():
            return True
        return False


solution = Solution()
print(solution.detectCapitalUse(word = "USA"))
print(solution.detectCapitalUse(word = "FlaG"))
print(solution.detectCapitalUse(word = "leetcode"))
print(solution.detectCapitalUse(word = "Google"))