# https://leetcode.com/problems/permutation-in-string/solutions/3138381/python3-sliding-window-comparision/
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter_1, counter_2 = Counter(s1), Counter()
        window = len(s1)
        for i, char in enumerate(s2):
            counter_2[char] += 1
            if i >= window:
                counter_2[s2[i-window]] -= 1
            if counter_1 == counter_2:
                return True
        return False


solution = Solution()
print(solution.checkInclusion(s1 = "ab", s2 = "eidbaooo"))
print(solution.checkInclusion(s1 = "ab", s2 = "eidboaoo"))