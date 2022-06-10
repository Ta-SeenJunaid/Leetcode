from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        c_position = []
        res = []
        for i in range(len(s)):
            if s[i]==c:
                c_position.append(i)
        for i in range(len(s)):
            res.append(min(abs(i-j) for j in c_position))
        return res


solution = Solution()
print(solution.shortestToChar(s="loveleetcode", c="e"))
print(solution.shortestToChar(s="aaab", c="b"))
