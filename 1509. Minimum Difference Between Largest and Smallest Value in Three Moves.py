# https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/editorial/?envType=daily-question&envId=2024-07-03
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        l_nums = len(nums)
        if l_nums <= 4:
            return 0
        smallest_four = sorted(heapq.nsmallest(4, nums))
        largest_four = sorted(heapq.nlargest(4, nums))
        min_dif = float('inf')
        for i in range(4):
            min_dif = min(min_dif, largest_four[i] - smallest_four[i])
        return min_dif
      
