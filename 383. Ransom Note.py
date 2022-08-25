class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        import collections
        ransomNote_dict = collections.Counter(ransomNote)
        magazine_dict = collections.Counter(magazine)
        for i in ransomNote_dict:
            if ransomNote_dict[i] > magazine_dict[i]:
                return False
        return True


solution = Solution()
print(solution.canConstruct(ransomNote = "a", magazine = "b"))
print(solution.canConstruct(ransomNote = "aa", magazine = "ab"))
print(solution.canConstruct(ransomNote = "aa", magazine = "aab"))
