# https://leetcode.com/problems/set-mismatch/solutions/4606148/python-1-liner-vs-c-no-hash-11-ms-beats-99-73 

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        return [sum(nums)-sum(set(nums)), len(nums)*(len(nums)+1)//2-sum(set(nums))]
        
