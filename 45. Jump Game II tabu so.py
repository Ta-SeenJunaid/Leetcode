# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         memo = {}
#         def dp(ix):
#             if ix >= len(nums) - 1:
#                 return 0
#             if ix in memo:
#                 return memo[ix]
#             if nums[ix] == 0:
#                 return float('inf')
#             temp = float("inf")
#             for i in range(1, nums[ix]+1):
#                 temp = min(temp, 1 + dp(ix+i))
#             memo[ix] = temp
#             return memo[ix]
#         return dp(0)

# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         n = len(nums)
#         temp = [float('inf')] * n
#         temp[0] = 0
#         for i in range(n):
#             for j in range(1, nums[i]+1):
#                 if (i+j) < n:
#                     temp[i+j] = min(temp[i+j], 1+temp[i])
#         return temp[-1]

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        current_min = 0
        farthest = 0
        jumps = 0
        for i in range(n-1):
            farthest = max(farthest, i + nums[i])
            if current_min == i:
                jumps += 1
                current_min = farthest
                if current_min >= n-1:
                    break
        return jumps
