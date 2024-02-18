class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        tabu = [[0 for _ in range(len(cuts)+2)] for _ in range(len(cuts)+2)]
        len_cuts = len(cuts)
        cuts.append(n)
        cuts.append(0)
        cuts.sort()
        for i in range(len_cuts, 0, -1):
            for j in range(1, len_cuts+1, 1):
                if i > j:
                    continue
                mini = float('inf')
                for idx in range(i, j+1, 1):
                    mini = min(mini, cuts[j+1] - cuts[i-1] + tabu[i][idx-1] + tabu[idx+1][j])
                tabu[i][j] = mini
        return tabu[1][len_cuts]
