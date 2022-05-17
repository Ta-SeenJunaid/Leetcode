from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max(len(sentence.split()) for sentence in sentences)


solution = Solution()
print(solution.mostWordsFound(
    sentences = ["alice and bob love leetcode",
                 "i think so too",
                 "this is great thanks very much"]))
print(solution.mostWordsFound(
    sentences = ["please wait",
                 "continue to fight",
                 "continue to win"]))
