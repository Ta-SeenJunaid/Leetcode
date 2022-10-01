from typing import List


class Solution:
    def __init__(self):
        self.temp = []

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.combination_sum_helper(candidates, target, [])
        result_len = len(self.temp)
        result = []
        for i in range(result_len):
            self.temp[i].sort()
            if self.temp[i] not in result:
                result.append(self.temp[i])
        return result


    def combination_sum_helper(self, candidates: List[int], target: int, current_candidates: List[int]):
        if target == 0:
            self.temp.append(current_candidates)
            return
        if target < 0:
            return

        for candidate in candidates:
            reminder = target - candidate
            temp_current_candidates = []
            temp_current_candidates = current_candidates + [candidate]
            if reminder >= 0:
                # print(current_candidates)
                self.combination_sum_helper(candidates, reminder, temp_current_candidates)


solution = Solution()
print(solution.combinationSum(candidates = [2,3,6,7], target = 7))
# print(solution.combinationSum(candidates = [2,3,5], target = 8))
# print(solution.combinationSum(candidates = [2], target = 1))