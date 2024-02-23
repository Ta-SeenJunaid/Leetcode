class Solution:
    def __init__(self):
        self.ans = []

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.recur(0, [], nums)
        return self.ans

    def recur(self, idx, cur_nums, nums):
        if idx == len(nums):
            self.ans.append(cur_nums)
            return
        self.recur(idx+1, cur_nums + [nums[idx]], nums)
        while idx+1 < len(nums) and nums[idx] == nums[idx+1]:
            idx += 1
        self.recur(idx+1, cur_nums, nums)
