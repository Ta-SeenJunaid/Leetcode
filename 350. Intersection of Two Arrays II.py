from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter
        counter_1 = Counter(nums1)
        common_element = []
        for num2 in nums2:
            if counter_1[num2] > 0:
                common_element.append(num2)
                counter_1[num2] -= 1

        return common_element


solution = Solution()
print(solution.intersect(nums1 = [1,2,2,1], nums2 = [2,2]))
print(solution.intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))
