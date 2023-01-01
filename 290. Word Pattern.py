class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        hash_table = {}
        if len(s) != len(pattern):
            return False
        for i in range(len(s)):
            if pattern[i] not in hash_table:
                hash_table[pattern[i]] = s[i]
            elif hash_table[pattern[i]] == s[i]:
                continue
            else:
                return False
        # for the case pattern = "abba", s = "dog dog dog dog")
        unique_value = set(hash_table.values())
        return len(unique_value) == len(hash_table)


solution = Solution()
print(solution.wordPattern(pattern = "abba", s = "dog cat cat dog"))
print(solution.wordPattern(pattern = "abba", s = "dog cat cat fish"))
print(solution.wordPattern(pattern = "aaaa", s = "dog cat cat dog"))
print(solution.wordPattern(pattern = "abba", s = "dog dog dog dog"))