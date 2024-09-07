# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        return self.check_path(head, root)

    def check_path(self, head, root):
        if root==None:
            return False
        if self.dfs_helper(head, root):
            return True
        return self.check_path(head, root.left) or self.check_path(head, root.right)

    def dfs_helper(self, head, root):
        if head==None:
            return True
        if root==None:
            return False
        if root.val != head.val:
            return False
        return self.dfs_helper(head.next, root.left) or self.dfs_helper(head.next, root.right)
        
