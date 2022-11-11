from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, nums_len, flag = 0, len(nums), 0
        while i < nums_len-1:
            if nums[i] == "-":
                return i
            if nums[i] == nums[i+1]:
                nums.pop(i+1)
                nums.append("-")
                flag = 1
                continue
            i += 1
        if flag:
            return len(nums[0:i])
        else:
            return nums_len


solution = Solution()
print(solution.removeDuplicates(nums = [1,1,2]))
print(solution.removeDuplicates(nums = [0,0,1,1,1,2,2,3,3,4]))