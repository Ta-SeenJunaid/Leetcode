# https://leetcode.com/problems/combination-sum-ii/solutions/4110275/clean-and-easy-solution-backtracking-based-python
# https://www.youtube.com/watch?v=G1fRTGRxXU8 

class Solution:
    def __init__(self):
        self.res = []

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        return []

    def recur(self, idx, target, path, candidates):
        if target == 0:
            self.res.append(path)
            return
        if target < 0 or idx >= len(candidates):
            return
        for i in range(idx, len(candidates)):
            self.recur(i+1, target-candidates[idx], path + [candidates[idx]], candidates)
        while idx < len(candidates) and candidates[idx]
