from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        graph_len = len(graph)
        ans = []
        stack = []
        for i in graph[0]:
            stack.append([0, i])
        while stack:
            temp = stack.pop()
            if temp[-1] == graph_len-1:
                ans.append(temp)
                continue
            for i in graph[temp[-1]]:
                temp2 = temp + [i]
                stack.append(temp2)
        return ans


solution = Solution()
print(solution.allPathsSourceTarget(graph = [[1,2],[3],[3],[]]))
print(solution.allPathsSourceTarget(graph = [[4,3,1],[3,2,4],[3],[4],[]]))





