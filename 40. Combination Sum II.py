# https://leetcode.com/problems/combination-sum-ii/solutions/4110275/clean-and-easy-solution-backtracking-based-python
# https://www.youtube.com/watch?v=G1fRTGRxXU8 

class Solution:
    def __init__(self):
        self.res = []

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.recur(0, target, [], candidates)
        return self.res

    def recur(self, idx, target, path, candidates):
        if target == 0:
            self.res.append(path)
            return
        if target < 0 or idx >= len(candidates):
            return
        self.recur(idx+1, target-candidates[idx], path + [candidates[idx]], candidates)
        while idx+1 < len(candidates) and candidates[idx] == candidates[idx+1]:
            idx += 1
        self.recur(idx+1, target, path, candidates)
