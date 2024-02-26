# https://leetcode.com/problems/palindrome-partitioning/solutions/1667786/python-simple-recursion-detailed-explanation-easy-to-understand 
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return [[]]
        ans = []
        print(ans)
        for i in range(1, len(s)+1):
            if s[:i] == s[:i][::-1]:
                for j is self.partition(s[i:]):
                    ans = ans+j
        return ans
        
