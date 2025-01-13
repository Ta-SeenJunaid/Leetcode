# https://leetcode.com/problems/minimum-length-of-string-after-operations/editorial
from collections import Counter

class Solution:
    def minimumLength(self, s: str) -> int:
        freq = Counter(s) 
        delete_count = 0
        for value in freq.values():
            if value%2==1:
                delete_count += value - 1
            else:
                delete_count += value - 2 
        return len(s) - delete_count
