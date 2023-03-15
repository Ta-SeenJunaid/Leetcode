from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                queue.append(node.left)
                queue.append(node.right)
            else:
                while queue:
                    if queue.pop(0):
                        return False
        return True


# class Solution:
#     def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
#         if not root:
#             return root
#         queue = [root]
#         while queue:
#             queue_len = len(queue)
#             has_grand_child = False
#             for i in range(queue_len):
#                 node = queue.pop(0)
#                 if i == 0 and node.left and node.left.left:
#                     has_grand_child = True
#
#                 print("node: "+ str(node.val) + " has_grand_child "
#                       + str(has_grand_child) + " i " + str(i) + " q len "+ str(queue_len))
#
#                 if i == 0 and node.left and not node.left.left and node:
#                     has_grand_child = True
#
#                 if has_grand_child and not(node.left and node.right):
#                     return False
#                 if not has_grand_child and not node.left and node.right:
#                     return False
#                 if not has_grand_child and node.left and not node.right and queue and queue[0].left:
#                     return False
#                 # if not has_grand_child and not node.right and i != queue_len-1:
#                 #     return False
#                 # if not has_grand_child and not node.right and i != queue_len-1:
#                 #     return False
#                 # if not has_grand_child and i == queue_len-1:
#                 #     return True
#                 if has_grand_child and node.left:
#                     queue.append(node.left)
#                 if has_grand_child and node.right:
#                     queue.append(node.right)
#                 # if node and node.left:
#                 #     queue.append(node.left)
#                 # if node and node.right:
#                 #     queue.append(node.right)
#         return True