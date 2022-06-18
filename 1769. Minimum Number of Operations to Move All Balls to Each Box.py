from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = [0]*len(boxes)
        for i in range(len(boxes)):
            for j in range(i):
                if boxes[i] == '1':
                    ans[j] += abs(i-j)
            for j in range(i, len(boxes)):
                if boxes[i] == '1':
                    ans[j] += abs(i-j)
        return ans


solution = Solution()
print(solution.minOperations(boxes = "110"))
print(solution.minOperations(boxes = "001011"))