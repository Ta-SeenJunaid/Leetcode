class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1, len2 = len(word1), len(word2)
        merged = ""
        if len1 >= len2:
            for i in range(0, len2):
                merged += word1[i]+word2[i]
            return merged + word1[len2:]
        else:
            for i in range(0, len1):
                merged += word1[i]+word2[i]
            return merged + word2[len1:]


solution = Solution()
print(solution.mergeAlternately(word1 = "abc", word2 = "pqr"))
print(solution.mergeAlternately(word1 = "ab", word2 = "pqrs"))
print(solution.mergeAlternately(word1 = "abcd", word2 = "pq"))
