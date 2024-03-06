class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ans = [[nums[0]]]
        for i in range(1, len(nums)):
            new_row = True
            for j in range(len(ans)):
                if nums[i] not in ans[j]:
                    ans[j].append(nums[i])
                    new_row = False
                    break
            if new_row:
                ans.append([nums[i]])
        return ans  
