class Solution:
    def __init__(self):
        self.memo = []

    def climbStairs(self, n: int) -> int:
        self.memo = [0 for _ in range(n)]
        return self.dp_helper(n, 0)

    def dp_helper(self, n: int, cur_n: int):
        if n == cur_n:
            return 1
        elif n < cur_n:
            return 0
        elif self.memo[cur_n] != 0:
            return self.memo[cur_n]
        else:
            self.memo[cur_n] = self.dp_helper(n, cur_n + 1) + self.dp_helper(n, cur_n + 2)
            return self.memo[cur_n]
