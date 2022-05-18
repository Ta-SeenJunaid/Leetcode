from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        answer = []
        for i in range(n):
            answer +=[nums[i], nums[i+n]]
        return answer


solution = Solution()
print(solution.shuffle(nums = [2,5,1,3,4,7], n = 3))
print(solution.shuffle(nums = [1,2,3,4,4,3,2,1], n = 4))
print(solution.shuffle(nums = [1,1,2,2], n = 2))