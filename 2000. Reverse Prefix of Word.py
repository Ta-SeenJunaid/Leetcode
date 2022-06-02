class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        i = word.find(ch)
        return word[:i + 1][::-1] + word[i + 1::]


solution = Solution()
print(solution.reversePrefix(word = "abcdefd", ch = "d"))
print(solution.reversePrefix(word = "xyxzxe", ch = "z"))
print(solution.reversePrefix(word = "abcd", ch = "z"))
