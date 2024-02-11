class Solution:
    def __init__(self):
        self.memo = None

    def minCost(self, n: int, cuts: List[int]) -> int:
        self.memo = [[-1 for _ in range(len(cuts)+1)] for _ in range(len(cuts)+1)]
        cuts.append(n)
        cuts.append(0)
        cuts.sort()
        return self.cutting(1, len(cuts)-2, cuts)

    def cutting(self, i, j, cuts):
        if i > j:
            return 0
        mini = float('inf')
        if self.memo[i][j] != -1:
            return self.memo[i][j]
        for idx in range(i, j+1):
            mini = min(mini, cuts[j+1] - cuts[i-1] + self.cutting(i, idx-1, cuts) + self.cutting(idx+1, j, cuts))
        self.memo[i][j] = mini
        return mini
