from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        not_matched = 0
        for word in words:
            for char in word:
                if char not in allowed:
                    not_matched += 1
                    break
        return len(words) - not_matched




solution = Solution()
print(solution.countConsistentStrings(allowed = "ab", words = ["ad","bd","aaab","baa","badab"]))
print(solution.countConsistentStrings(allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]))
print(solution.countConsistentStrings(allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]))