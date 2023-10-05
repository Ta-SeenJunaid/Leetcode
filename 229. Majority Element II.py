class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        element_count = Counter(nums)
        threshold = len(nums) // 3
        res = []
        for element, count in element_count.items():
            if count > threshold:
                res.append(element)
        return res
        
