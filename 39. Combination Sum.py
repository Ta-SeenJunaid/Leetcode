class Solution:
    def __init__(self):
        self.ans = []

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.recur(0, target, [], candidates)
        return self.ans

    def recur(self, idx, cur_target, cur_list, candidates):
        if cur_target == 0:
            if cur_list not in self.ans:
                self.ans.append(cur_list)
                return
        if cur_target < 0 or idx >= len(candidates):
            return
        self.recur(idx+1, cur_target, cur_list, candidates)
        self.recur(idx, cur_target-candidates[idx], cur_list + [candidates[idx]], candidates)
