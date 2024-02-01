# https://leetcode.com/problems/count-good-numbers/solutions/1314522/well-explained-4-lines-97-faster-easily-understandable 
# https://leetcode.com/problems/count-good-numbers/solutions/3788394/easy-to-understand-code-one-liner

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        return (pow(5,(n + 1)//2,1000000007)*pow(4,n//2,1000000007))%1000000007
