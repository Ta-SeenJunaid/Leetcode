# https://leetcode.com/problems/find-the-winner-of-the-circular-game/editorial/?envType=daily-question&envId=2024-07-08
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        ans = 0
        for i in range(2, n+1):
            ans = (ans + k) % i
        return ans + 1
