from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        sorted_list = []
        for i in matrix:
            for j in i:
                sorted_list.append(j)
        sorted_list.sort()
        return sorted_list[k-1]


solution = Solution()
print(solution.kthSmallest(matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
))
print(solution.kthSmallest(matrix = [[-5]], k = 1))
