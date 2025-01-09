# class Solution:
#     def prefixCount(self, words: List[str], pref: str) -> int:
#         count = 0
#         l_p = len(pref)
#         for word in words:
#             if word[:l_p] == pref:
#                 count += 1
#         return count
        
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for word in words:
            if word.startswith(pref):
                count += 1
        return count
