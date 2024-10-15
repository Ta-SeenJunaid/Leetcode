# https://www.youtube.com/watch?v=EYeR-_1NRlQ
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans, temp = [],[]
        def k_sum(k, start, target):
            if k!= 2:
                for i in range(start, len(nums)-k +1):
                    if i != start and nums[i] == nums[i-1]:
                        continue
                    temp.append(nums[i])
                    k_sum(k-1, i+1, target-nums[i])
                    temp.pop()
                return

            l, r = start, len(nums)-1
            while l < r:
                sum_ = nums[l] + nums[r]
                if sum_ < target:
                    l += 1
                elif sum_ > target:
                    r -= 1
                else:
                    ans.append(temp + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        k_sum(4, 0, target)
        return ans
        
