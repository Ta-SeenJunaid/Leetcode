from typing import List


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        j = []

        for i in range(0, len(nums)):
            if nums[i]==key:
                j.append(i)

        ans = []

        for i in range(0, len(nums)):
            for b in range(0, len(j)):
                # print("i: ", nums[i])
                # print("j: ", nums[j[b]])
                if abs(i-j[b]) <= k:
                    ans.append(i)

        ans = list(set(ans))
        ans.sort()
        return ans


solution = Solution()
print(solution.findKDistantIndices(nums = [3,4,9,1,3,9,5], key = 9, k = 1))
print(solution.findKDistantIndices(nums = [2,2,2,2,2], key = 2, k = 2))

