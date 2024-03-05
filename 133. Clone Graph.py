# https://leetcode.com/problems/clone-graph/solutions/1792858/python3-iterative-bfs-beats-98-explained 

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        queue = [node]
        visited = {node.val:Node(node.val, [])}
        while queue:
            cur_node = queue.pop(0)
            copy_node = visited[cur_node.val]
            for nei in cur_node.neighbors:
                if nei.val not in visited:
                    visited[nei.val] = Node(nei.val, [])
                    queue.append(nei)
                copy_node.neighbors.append(visited[nei.val])
        return visited[node.val]
        
