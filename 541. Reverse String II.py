# https://leetcode.com/problems/reverse-string-ii/solutions/482766/easy-python-solution-beat-98-time-and-100-space/


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s_len = len(s)
        if s_len < k:
            return s[::-1]
        if s_len >= k and s_len < 2*k:
            return s[:k][::-1] + s[k:]
        result = ""
        for i in range(0, s_len, 2*k):
            result += s[i:i+k][::-1] + s[i+k:i+2*k]
        return result


solution = Solution()
print(solution.reverseStr(s = "abcdefg", k = 2))
print(solution.reverseStr(s = "abcd", k = 2))