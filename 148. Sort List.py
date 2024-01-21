# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        l_val = []
        while curr:
            l_val.append(curr.val)
            curr = curr.next
        l_val.sort()
        curr = head
        for i in l_val:
            curr.val = i
            curr = curr.next
        return head
