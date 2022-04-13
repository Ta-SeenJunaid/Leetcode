class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """

        nums1 = list(set(nums1))
        nums2 = list(set(nums2))

        return1 = list(x for x in nums1 if x not in nums2)
        return2 = list(x for x in nums2 if x not in nums1)

        return [return1, return2]


solution = Solution()
print(solution.findDifference(nums1 = [1,2,3], nums2 = [2,4,6]))
print(solution.findDifference(nums1 = [1,2,3,3], nums2 = [1,1,2,2]))