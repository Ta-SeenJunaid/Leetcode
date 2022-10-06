from typing import List


class Solution:
    def __init__(self):
        self.memo = {}

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.dp_helper(s, wordDict)

    def dp_helper(self, s: str, wordDict: List[str]):
        if s in self.memo:
            return self.memo[s]
        if s == "":
            return True
        for word in wordDict:
            if s.find(word) == 0:
                if self.dp_helper(s[len(word)::], wordDict):
                    self.memo[s] = True
                    return True
        self.memo[s] = False
        return False


solution = Solution()
print(solution.wordBreak(s = "leetcode", wordDict = ["leet","code"]))
print(solution.wordBreak(s = "applepenapple", wordDict = ["apple","pen"]))
print(solution.wordBreak(s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]))
print(solution.wordBreak(s = "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef" ,
                             wordDict = ["e", "ee", "eee", "eeee", "eeeee", "eeeeee", "eeeeeee"]))