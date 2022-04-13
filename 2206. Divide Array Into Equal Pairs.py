
class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        import collections

        counter = collections.Counter(nums)

        for i in counter.values():
            if i%2 != 0:
                return False

        return True


solution = Solution()
print(solution.divideArray(nums = [3,2,3,2,2,2]))
print(solution.divideArray(nums = [1,2,3,4]))