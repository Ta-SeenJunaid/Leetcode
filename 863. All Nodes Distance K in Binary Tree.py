# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent_track = {}
        parent_track[root] = None
        queue_pa_find = [root]
        while queue_pa_find:
            for _ in range(len(queue_pa_find)):
                node = queue_pa_find.pop(0)
                if node:
                    if node.left:
                        parent_track[node.left] = node
                        queue_pa_find.append(node.left)
                    if node.right:
                        parent_track[node.right] = node
                        queue_pa_find.append(node.right)
        visited = set()
        cur_level = 0
        queue = [target]
        while queue:
            if cur_level == k:
                break
            for _ in range(len(queue)):
                node = queue.pop(0)
                visited.add(node.val)
                if node.left and node.left.val not in visited:
                    queue.append(node.left)
                if node.right and node.right.val not in visited:
                    queue.append(node.right)
                if parent_track[node] and parent_track[node].val not in visited:
                    queue.append(parent_track[node])
            cur_level += 1
        res = []
        for node in queue:
            res.append(node.val)
        return res
        
