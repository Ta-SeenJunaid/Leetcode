class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26


solution = Solution()
print(solution.checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))
print(solution.checkIfPangram("leetcode"))