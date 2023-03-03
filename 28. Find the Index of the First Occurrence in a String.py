class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


solution = Solution()
print(solution.strStr(haystack = "sadbutsad", needle = "sad"))
print(solution.strStr(haystack = "leetcode", needle = "leeto"))