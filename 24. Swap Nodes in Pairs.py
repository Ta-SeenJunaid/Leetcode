# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            ans = head.next
        else:
            return head
        prev = None
        while head:
            first = head
            second = head.next
            if head.next and head.next.next:
                first.next = head.next.next
            else:
                first.next = None
            if second:
                second.next = first
                if prev:
                    prev.next = second
            prev = head
            head = first.next
        return ans
        
