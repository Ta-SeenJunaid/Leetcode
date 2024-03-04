"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        queue = [root]
        while queue:
            q_len = len(queue)
            for i in range(q_len):
                node = queue.pop(0)
                if node:
                    if i < q_len - 1:
                        node.next = queue[0]
                    else:
                        node.next = None
                    if node.left != None:
                        queue.append(node.left)
                    if node.right != None:
                        queue.append(node.right)
        return root
        
