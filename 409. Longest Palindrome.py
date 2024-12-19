class Solution:
    def longestPalindrome(self, s: str) -> int:
        odd_pelindrome = False
        ans = 0
        dictc = defaultdict(int)
        for c in s:
            dictc[c]  += 1
        for key in dictc:
            if dictc[key]%2 == 0:
                ans += dictc[key]
            else:
                odd_pelindrome = True
                ans += dictc[key] - 1
        if odd_pelindrome:
            ans += 1
        return ans
        
