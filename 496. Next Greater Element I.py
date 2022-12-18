from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        memory = {}
        stack = []
        res = []
        for i in nums2:
            while stack and i > stack[-1]:
                value = stack.pop()
                memory[value] = i
            stack.append(i)
        for i in nums1:
            if i in memory:
                res.append(memory[i])
            else:
                res.append(-1)
        return res


solution = Solution()
print(solution.nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2]))
print(solution.nextGreaterElement(nums1 = [2,4], nums2 = [1,2,3,4]))
