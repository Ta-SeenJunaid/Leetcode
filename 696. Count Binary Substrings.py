# https://www.youtube.com/watch?v=0O2D-AS2-UI

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans = 0
        pre_count = 0
        s_len = len(s)
        i = 0
        while i < s_len:
            current_count = 1
            while i < s_len-1 and s[i]==s[i+1]:
                current_count += 1
                i += 1
            if pre_count > 0:
                ans += min(pre_count, current_count)
            pre_count = current_count
            i += 1
        return ans


solution = Solution()
print(solution.countBinarySubstrings(s = "00110011"))
print(solution.countBinarySubstrings(s = "10101"))
