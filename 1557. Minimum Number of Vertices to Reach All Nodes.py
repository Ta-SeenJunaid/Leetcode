from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # vertices whose indegree is zero
        track = [0]*n
        for u, v in edges:
            track[v] += 1
        result = []
        for index, value in enumerate(track):
            if value == 0:
                result.append(index)
        return result


solution = Solution()
print(solution.findSmallestSetOfVertices(n = 6,
                                         edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]))
print(solution.findSmallestSetOfVertices(n = 5,
                                         edges = [[0,1],[2,1],[3,1],[1,4],[2,4]]))