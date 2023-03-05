# https://www.youtube.com/watch?v=ovg-nBiQRGo
from collections import defaultdict
from typing import List


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        arr_len = len(arr)
        ans = 0
        value_to_index = defaultdict(list)
        for i, value in enumerate(arr):
            value_to_index[value].append(i)
        queue = []
        visited = set()
        queue.append(0)
        visited.add(0)
        while queue:
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node == arr_len-1:
                    return ans
                neighbors = []
                if node > 0:
                    neighbors.append(node - 1)
                if node < arr_len-1:
                    neighbors.append(node + 1)
                if arr[node] in value_to_index:
                    neighbors.extend(value_to_index[arr[node]])
                     # It's crucial
                    del value_to_index[arr[node]]
                for i in neighbors:
                    if i not in visited:
                        queue.append(i)
                        visited.add(i)
            ans += 1
        return ans


solution = Solution()
print(solution.minJumps(arr = [100,-23,-23,404,100,23,23,23,3,404]))
print(solution.minJumps(arr = [7]))
print(solution.minJumps(arr = [7,6,9,6,9,6,9,7]))