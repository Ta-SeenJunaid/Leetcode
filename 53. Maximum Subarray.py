class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]

        return max(nums)


solution = Solution()
print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))