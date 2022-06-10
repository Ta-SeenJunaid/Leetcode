class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_elements = []
        left_p, max_unique_elements = 0, 0
        for right_p in range(len(s)):
            while s[right_p] in unique_elements:
                unique_elements.remove(s[left_p])
                left_p += 1
            unique_elements.append(s[right_p])
            max_unique_elements = max(max_unique_elements, len(unique_elements))
        return max_unique_elements


solution = Solution()
print(solution.lengthOfLongestSubstring(s = "abcabcbb"))
print(solution.lengthOfLongestSubstring(s = "bbbbb"))
print(solution.lengthOfLongestSubstring(s = "pwwkew"))