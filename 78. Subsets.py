class Solution:
    def __init__(self):
        self.output = []

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.recur(0, [], nums)
        return self.output

    def recur(self, idx, cur, nums):
        if idx == len(nums):
            self.output.append(cur)
            return
        self.recur(idx+1, cur + [nums[idx]], nums)
        self.recur(idx+1, cur, nums)
        return
