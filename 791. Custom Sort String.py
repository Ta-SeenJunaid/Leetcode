# https://leetcode.com/problems/custom-sort-string/solutions/4856371/100-beats-hash-table-easy-explanation-c-java-python 

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ans = ""
        dict_s = defaultdict(int)
        for ch in s:
            dict_s[ch] += 1
        for ch in order:
            ans += ch*dict_s[ch]
            del dict_s[ch]
        for ch in dict_s:
            ans += ch*dict_s[ch]
        return ans
        
