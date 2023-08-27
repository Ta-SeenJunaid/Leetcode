class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low, high= 1, max(nums)
        ans = high
        while low <= high:
            mid = (low+high)//2
            if self.is_possible(nums, threshold, mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans 
    
    def is_possible(self, nums: List[int], threshold:int, current_num) -> bool:
        temp = 0
        for num in nums:
            temp += ceil(num/current_num)
        if temp <= threshold:
            return True
        else:
            return False
