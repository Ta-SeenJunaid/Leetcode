# https://www.youtube.com/watch?v=iYOm3anZjlU&t=1s
from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        word_dict= {}
        for i in range(len(order)):
            word_dict[order[i]] = i
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            for j in range(min(len(word1), len(word2))):
                if word_dict[word1[j]] < word_dict[word2[j]]:
                    break
                elif word_dict[word1[j]] > word_dict[word2[j]]:
                    return False
                elif j== min(len(word1), len(word2)-1) and len(word1) > len(word2):
                    return False
        return True


solution = Solution()
print(solution.isAlienSorted(words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"))
print(solution.isAlienSorted(words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"))
print(solution.isAlienSorted(words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"))