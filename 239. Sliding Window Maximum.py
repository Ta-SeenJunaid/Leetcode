# https://www.youtube.com/watch?v=DfljaUwZsOk
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r, result = 0, 0, []
        queue = []
        while r < len(nums):
            while queue and nums[r] > nums[queue[-1]]:
                queue.pop()
            queue.append(r)
            if l > queue[0]:
                queue.pop(0)
            if r + 1 >= k:
                result.append(nums[queue[0]])
                l += 1
            r += 1
        return result

# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         l, r, result = 0, 0, []
#         max_num = 0
#         queue = []
#         for i in range(len(nums)):
#             r += 1
#             if r - l != k:
#                 if nums[i] >= max_num:
#                     max_num = nums[i]
#                     queue.append(max_num)
#                 if queue and nums[l] == queue[0] and max_num != queue[0]:
#                     queue.pop(0)
#             if r-l == k:
#                 # print(nums[l:r])
#                 # result.append(max((nums[l:r])))
#                 if nums[i] >= max_num:
#                     max_num = nums[i]
#                     queue.append(max_num)
#                 if queue:
#                     result.append(queue[-1])
#                 else:
#                     result.append(max_num)
#                 # print(i, l)
#                 if queue and nums[l] == queue[0]:
#                     queue.pop(0)
#                 l += 1
#         return result



solution = Solution()
print(solution.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))
print(solution.maxSlidingWindow(nums = [1], k = 1))

print(solution.maxSlidingWindow(nums = [3, 1,-1,-3,5,3,6,7], k = 3))
print(solution.maxSlidingWindow(nums = [1,-1, 3,-3,5,3,6,7], k = 3))
print(solution.maxSlidingWindow(nums = [1,-1], k = 1))

