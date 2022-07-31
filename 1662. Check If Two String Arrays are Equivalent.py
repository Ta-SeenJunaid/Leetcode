from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        if ''.join(word1) == ''.join(word2):
            return True
        else:
            return False


solution = Solution()
print(solution.arrayStringsAreEqual(word1 = ["ab", "c"], word2 = ["a", "bc"]))
print(solution.arrayStringsAreEqual(word1 = ["a", "cb"], word2 = ["ab", "c"]))
print(solution.arrayStringsAreEqual(word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]))
