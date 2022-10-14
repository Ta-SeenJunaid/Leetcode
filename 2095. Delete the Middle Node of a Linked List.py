# https://www.youtube.com/watch?v=tVyxhuKqQBs
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        prev = None
        slow_p = first_p = head
        while first_p and first_p.next:
            prev = slow_p
            slow_p = slow_p.next
            first_p = first_p.next.next
        if slow_p.next:
            prev.next = slow_p.next
        else:
            prev.next = None
        return head