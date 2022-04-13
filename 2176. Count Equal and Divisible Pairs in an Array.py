class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        counter = 0
        for i in range(0,len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j] and (i*j)%k == 0:
                    counter += 1

        return counter


solution = Solution()
print(solution.countPairs(nums = [3,1,2,2,2,1,3], k = 2))
print(solution.countPairs(nums = [1,2,3,4], k = 1))