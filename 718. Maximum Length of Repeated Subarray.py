from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        table = [[0 for _ in range(n+1)] for _ in range(m+1) ]
        max_val = 0
        for row in range(1, m+1):
            for col in range(1, n+1):
                if nums2[row - 1] == nums1[col - 1]:
                    table[row][col] = 1 + table[row-1][col-1]
                    if table[row][col] > max_val:
                        max_val = table[row][col]
        return max_val


solution = Solution()
print(solution.findLength(nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]))
print(solution.findLength(nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]))