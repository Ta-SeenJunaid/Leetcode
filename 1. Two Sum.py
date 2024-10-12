class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in dictionary:
                return  [i, dictionary[compliment]]
            dictionary[nums[i]] = i
        return []
        
