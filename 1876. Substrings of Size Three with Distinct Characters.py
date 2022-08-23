class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        result = 0
        for a, b, c in zip(s, s[1:], s[2:]):
            if a == b or b == c or c == a:
                continue
            result += 1
        return result


solution = Solution()
print(solution.countGoodSubstrings(s = "xyzzaz"))
print(solution.countGoodSubstrings(s = "aababcabc"))
