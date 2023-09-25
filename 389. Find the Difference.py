# https://leetcode.com/problems/find-the-difference/solutions/4086631/99-78-xor-sum/?envType=daily-question&envId=2023-09-25
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ans = 0
        for char in s + t:
            ans ^= ord(char)
        return chr(ans) 
