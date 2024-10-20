# chatgpt
class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        prefix_sum = [0]* (n+1)
        res = []
        for i in range(1, (n+1)):
            prefix_sum[i] = prefix_sum[i-1] + nums[i-1]
        for query in queries:
            pos = bisect_left(nums, query)
            left_sum = query*pos - prefix_sum[pos]
            right_sum = (prefix_sum[n] - prefix_sum[pos]) - query * (n-pos)
            res.append(left_sum+right_sum)
        return res
        
