# https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/solutions/4489526/better-than-100-c-java-python-javascript-2-approaches-explained 

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        freq = [0] * (len(nums)+1)
        ans = []
        print(freq)
        for num in nums:
            if freq[num] >= len(ans):
                ans.append([])
            ans[freq[num]].append(num)
            freq[num] += 1
        return ans
       
