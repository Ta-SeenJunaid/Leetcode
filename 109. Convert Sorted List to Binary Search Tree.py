from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        return self.bst(nums)


    def bst(self, nums: Optional[list]):
        if nums is None or len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        mid = len(nums)//2
        root = TreeNode(nums[mid])
        root.left = self.bst(nums[:mid])
        root.right = self.bst(nums[mid+1:])
        return root


# class Solution:
#     def sortedListToBST(self, head: ListNode) -> TreeNode:
#         if not head:
#             return None
#         if not head.next:
#             return TreeNode(head.val)
#         middle = self.getMiddle(head)
#         root = TreeNode(middle.val)
#         root.right = self.sortedListToBST(middle.next)
#         middle.next = None
#         root.left = self.sortedListToBST(head)
#         return root
#
#     def getMiddle(self, head: ListNode) -> ListNode:
#         fast = head
#         slow = head
#         prev = None
#         while fast and fast.next:
#             fast = fast.next.next
#             prev = slow
#             slow = slow.next
#         if prev:
#             prev.next = None
#         return slow

