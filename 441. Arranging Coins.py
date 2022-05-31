class Solution:
    def arrangeCoins(self, n: int) -> int:
        i= 0
        while n >= 0:
            i +=1
            n=n-i
        if n == 0:
            return i
        else:
            return i-1


solution = Solution()
print(solution.arrangeCoins(n=5))
print(solution.arrangeCoins(n=8))
print(solution.arrangeCoins(n=6))

