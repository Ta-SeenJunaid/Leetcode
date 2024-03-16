# https://www.youtube.com/watch?v=agB1LyObUNE
# https://leetcode.com/problems/contiguous-array/solutions/4881359/easy-explanation-hashmap-beats-93-29-c-java-python3-kotlin

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        cur_sum = 0
        max_len = 0
        p_dict = {}
        for i in range(len(nums)):
            cur_sum += 1 if nums[i]==1 else -1
            if cur_sum == 0:
                max_len = i+1
            elif cur_sum in p_dict:
                max_len = max(max_len, i - p_dict[cur_sum])
            else:
                p_dict[cur_sum] = i
        return max_len

        
